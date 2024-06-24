from utils import NewResponse
from utils.common_jwt_authentication import NewJWTAuthentication
from utils.common_mixins import *
from . import models
from ua_parser import user_agent_parser
from .tools.seriaizer import PostSerializer
from .tools import LoginSerializer, UserSerializer, AdminPermission, OnlineSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


class LoginView(GenericViewSet):

    serializer_class = LoginSerializer

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.store_online_user()
        return NewResponse(message='login success!', token=serializer.context['token'], result=serializer.validated_data)

    @transaction.atomic
    def store_online_user(self):
        # 获取登录用户平台信息
        user_agent = self.request.META.get('HTTP_USER_AGENT')
        user_agent_info = user_agent_parser.Parse(user_agent)
        if 'Mozilla' in user_agent_info.get('string'):
            browser = '-'.join((user_agent_info['user_agent']['family'], user_agent_info['user_agent']['major']))
        else:
            browser = user_agent_info.get('string')

        # 登陆成功后添加到在线用户表
        try:
            models.OnlineUser.objects.update_or_create(
                user_id=self.request.user.id,
                defaults={
                    'ip': self.request.META['REMOTE_ADDR'],
                    'token': self.request.user.cache_key,
                    'browser': browser,
                    'is_deleted': False,
                }
            )
        except Exception as e:
            ...


class UserView(
    GenericViewSet,
    NewListMixin,
):
    authentication_classes = (NewJWTAuthentication, )
    permission_classes = (IsAuthenticated, AdminPermission)

    serializer_class = UserSerializer
    queryset = models.Users.objects.filter(is_deleted=False).all()


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
