from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from utils.common_exception import CreateException
from .. import models
import re
from utils.common_function import token_cache_key
from django.conf import settings
from django.core.cache import cache
from django.db.models import Q
from django.db import transaction


class UserMixin:

    re_tuple = (
        r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$',
        r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',
    )

    @staticmethod
    def _valid_list(valid: list):
        """
        检测前端传入的角色和职位列表格式是否正确
        :param valid:
        :return:
        """
        for val in valid:
            if not isinstance(val, int):
                raise serializers.ValidationError(f'{valid} format error!')

    def _match_account(self, account: str):
        """
        检测账户名是否正确
        :param account:
        :return:
        """
        if re.match(self.re_tuple[0], account):
            user = models.Users.objects.filter(phone=account).first()
        elif re.match(self.re_tuple[1], account):
            user = models.Users.objects.filter(email=account).first()
        else:
            user = models.Users.objects.filter(username=account).first()
        return user

    def check_user(self, account: str, password: str):
        """
        检测用户是否存在
        :param account:
        :param password:
        :return:
        """
        if not account or not password:
            raise serializers.ValidationError('account or password is None!')

        user = self._match_account(account)
        if not user:
            raise serializers.ValidationError('this account is not exist!')

        if not user.check_password(password):
            raise serializers.ValidationError('password is wrong!')

        if not user.is_active:
            raise serializers.ValidationError('account is inactive!')

        return user

    @staticmethod
    def generate_token(user: models.Users):
        """
        签发token, 并存储在redis中, cache.set()方法默认过期时间为300s！！！
        :param user:
        :return:
        """
        token = RefreshToken.for_user(user)
        user.cache_key = token_cache_key(token)
        cache.set(user.cache_key, str(token), timeout=86400)  # 一天
        return token

    @staticmethod
    def roles_or_posts(obj, default: str):
        """
        获取用户角色和岗位信息
        :param obj: user object
        :param default: roles or posts
        :return:
        """
        post_pk = [rel.post_id for rel in models.UserPosts.objects.filter(user_id=obj.pk).all()]
        role_pk = [rel.role_id for rel in models.UserRoles.objects.filter(user_id=obj.pk).all()]

        dic = {
            'roles': [role.name for role in models.Role.objects.filter(pk__in=role_pk).all()],
            'posts': [post.name for post in models.Post.objects.filter(pk__in=post_pk).all()],
        }
        return dic.get(default)


class LoginSerializer(serializers.Serializer, UserMixin):
    account = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField()

    def validate(self, attrs):
        account = attrs.get('account')
        password = attrs.get('password')
        invalid_token = attrs.get('token')
        user = self.check_user(account, password)

        if invalid_token != 'undefined':   # 每次登录删除旧token
            if cache.get(token_cache_key(invalid_token)):
                cache.delete(token_cache_key(invalid_token))

        self.context['request'].user = user  # 登录成功全局user
        self.context['token'] = str(self.generate_token(user))

        return {
            'id': user.id,
            'username': user.username,
            'avatar': ''.join((settings.SERVER_URL, settings.MEDIA_URL, str(user.avatar))),
            'is_active': user.is_active,
        }


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ('name', 'desc')


class UserSerializer(serializers.ModelSerializer, UserMixin):

    class Meta:
        model = models.Users
        fields = (
            'id', 'username', 'password', 'posts', 'roles', 'email',
            'gender', 'avatar', 'phone', 'created_at', 'created_by', 'is_active'
        )

    posts = serializers.SerializerMethodField(read_only=True)
    roles = serializers.SerializerMethodField(read_only=True)

    def get_posts(self, obj):
        return self.roles_or_posts(obj, 'posts')

    def get_roles(self, obj):
        return self.roles_or_posts(obj, 'roles')


class UserActionSerializer(serializers.ModelSerializer, UserMixin):

    roles = serializers.ListField(write_only=True)
    posts = serializers.ListField(write_only=True)

    class Meta:
        model = models.Users
        fields = ('username', 'email', 'gender', 'phone', 'roles', 'posts')

        extra_kwargs = {
            'username': {'write_only': True},
            'email': {'write_only': True},
            'gender': {'write_only': True},
            'phone': {'write_only': True},
        }

    def validate(self, attrs):
        email = attrs.get('email')
        phone = attrs.get('phone')
        posts = attrs.get('posts')
        roles = attrs.get('roles')

        # 检测邮箱、手机号
        if not re.match(self.re_tuple[0], phone) or not re.match(self.re_tuple[1], email):
            raise serializers.ValidationError('phone or email is wrong!')

        # 检测用户是否存在
        if models.Users.objects.filter(Q(email=email) | Q(phone=phone)).exists():
            raise serializers.ValidationError('email or phone is exist!')

        self._valid_list(posts)
        self._valid_list(roles)
        return attrs

    def create(self, validated_data):
        posts = validated_data.pop('posts')
        roles = validated_data.pop('roles')
        cache.add('default_password', '123456')

        # 涉及多表操作，添加事务
        with transaction.atomic():
            try:
                new_user = models.Users.objects.create(**validated_data)

                new_user.set_password(cache.get('default_password'))
                new_user.save()
                if posts:
                    user_posts = [models.UserPosts(user_id=new_user.pk, post_id=post_id) for post_id in posts]
                    models.UserPosts.objects.bulk_create(user_posts)

                if roles:
                    user_roles = [models.UserRoles(user_id=new_user.pk, role_id=role_id) for role_id in roles]
                    models.UserRoles.objects.bulk_create(user_roles)

            except CreateException as ex:
                ...
        return new_user


class OnlineSerializer(serializers.ModelSerializer):

    username = serializers.CharField(read_only=True)

    class Meta:
        model = models.OnlineUser
        fields = ('id', 'username', 'ip', 'addr', 'updated_at', 'token', 'browser')
