from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .. import models
import re
from django.conf import settings


class UserMixin:

    re_tuple = (
        r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$',
        r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',
    )

    def _match_account(self, account):
        if re.match(self.re_tuple[0], account):
            user = models.Users.objects.filter(phone=account).first()
        elif re.match(self.re_tuple[1], account):
            user = models.Users.objects.filter(email=account).first()
        else:
            user = models.Users.objects.filter(username=account).first()
        return user

    def check_user(self, account: str, password: str):
        if not account or not password:
            raise serializers.ValidationError('account or password is None!')

        user = self._match_account(account)
        if not user:
            raise serializers.ValidationError('this account is not exist!')

        if not user.check_password(password):
            raise serializers.ValidationError('password is wrong!')

        return user

    @staticmethod
    def generate_token(user):
        token = RefreshToken.for_user(user)
        return token

    @staticmethod
    def roles_or_posts(obj, default):
        post_pk = [post.pk for post in models.UserPosts.objects.filter(user_id=obj.pk).all()]
        role_pk = [role.pk for role in models.UserRoles.objects.filter(user_id=obj.pk).all()]

        dic = {
            'roles': [role.name for role in models.Role.objects.filter(pk__in=role_pk).all()],
            'posts': [post.name for post in models.Post.objects.filter(pk__in=post_pk).all()],
        }
        return dic.get(default)


class LoginSerializer(serializers.Serializer, UserMixin):
    account = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        account = attrs.get('account')
        password = attrs.get('password')
        user = self.check_user(account, password)

        post_list = self.roles_or_posts(user, 'posts')
        self.context['request'].user = user
        return {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'posts': post_list,
            'email': user.email,
            'phone': user.phone,
            'avatar': ''.join((settings.SERVER_URL, settings.MEDIA_URL, str(user.avatar))),
            'created_at': user.created_at,
            'created_by': user.created_by,
            'is_active': user.is_active,
            'token': str(self.generate_token(user)),
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


# class UserActionSerializer(serializers.ModelSerializer, UserMixin):
#
#     class Meta:
#         model = models.Users
#         fields = ('username', 'email', 'phone', 'roles', 'posts',)

