from utils import NewResponse
from utils.common_jwt_authentication import NewJWTAuthentication
from utils.common_mixins import *
from utils.common_function import token_cache_key
from . import models
from . import tasks
from ua_parser import user_agent_parser
from .tools.seriaizer import PostSerializer
from .tools import (LoginSerializer, UserSerializer, AdminPermission,
                    OnlineSerializer, UserActionSerializer, UserFilter, UpdatePasSerializer)
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache


class LoginView(GenericViewSet):

    serializer_class = LoginSerializer

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.store_online_user()
        return NewResponse(message='login success!', token=serializer.context['token'], result=serializer.validated_data)

    def store_online_user(self):
        # 获取登录用户平台信息
        user_agent = self.request.META.get('HTTP_USER_AGENT')
        user_agent_info = user_agent_parser.Parse(user_agent)
        if 'Mozilla' in user_agent_info.get('string'):
            browser = '-'.join((user_agent_info['user_agent']['family'], user_agent_info['user_agent']['major']))
        else:
            browser = user_agent_info.get('string')

        # 登陆成功后添加到在线用户表
        models.OnlineUser.objects.update_or_create(
            user_id=self.request.user.id,
            defaults={
                'ip': self.request.META['REMOTE_ADDR'],
                'token': self.request.user.cache_key,
                'browser': browser,
                'is_deleted': False,
            }
        )


class UserView(
    GenericViewSet,
    NewListMixin,
    NewCreateMixin,
    NewUpdateMixin,
    NewDeleteMixin,
    NewRetrieveMixin
):
    authentication_classes = (NewJWTAuthentication, )
    permission_classes = (IsAuthenticated, AdminPermission)

    queryset = models.Users.objects.filter(is_deleted=False).all()
    filter_backends = (UserFilter,)

    def get_queryset(self):
        user_queryset = cache.get('user_queryset')
        if not user_queryset:
            cache.set('user_queryset', self.queryset, timeout=3600)
            user_queryset = self.queryset
        return user_queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        else:
            return UserActionSerializer

    def perform_create(self, serializer):
        serializer.save()
        # 新增用户，更新缓存
        tasks.update_user_queryset.delay()

        # 通知用户
        tasks.send_email.delay('欢迎加入汪汪立功队！您的初始密码为123456，请尽快登录并修改密码!', serializer.context['email'])


class UpdatePassView(GenericViewSet, NewUpdateMixin):
    authentication_classes = (NewJWTAuthentication, )
    permission_classes = (IsAuthenticated, AdminPermission)
    queryset = models.Users.objects.filter(is_deleted=False).all()
    serializer_class = UpdatePasSerializer

    def perform_update(self, serializer):
        serializer.save()
        cache.delete(
            token_cache_key(
                models.OnlineUser.objects.filter(is_deleted=False, user=self.request.user).first().token
            )
        )
        tasks.send_email.delay('您的密码修改成功, 请重新登录!', serializer.context['email'])


class PostView(
    GenericViewSet,
    NewListMixin,
    NewCreateMixin,
    NewUpdateMixin,
    NewDeleteMixin,
    NewRetrieveMixin,
):
    authentication_classes = (NewJWTAuthentication, )
    permission_classes = (IsAuthenticated, AdminPermission)
    serializer_class = PostSerializer
    queryset = models.Post.objects.filter(is_deleted=False).all()


class OnlineUserView(
    GenericViewSet,
    NewListMixin,
    NewRetrieveMixin,

):
    authentication_classes = (NewJWTAuthentication, )
    permission_classes = (IsAuthenticated, AdminPermission)
    serializer_class = OnlineSerializer
    queryset = models.OnlineUser.objects.filter(is_deleted=False).all()
