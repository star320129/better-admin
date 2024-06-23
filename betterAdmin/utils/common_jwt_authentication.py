from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.utils import get_md5_hash_password
from django.core.cache import cache
from src.Users.models import Users
from utils.common_function import token_cache_key


class NewJWTAuthentication(JWTAuthentication):
    """
    基于自定义Users表和JWTAuthentication编写 token认证
    """
    def authenticate(self, request):
        header, token = self.get_authorization(request)
        if not header or header != 'Bearer':    # 令牌
            raise AuthenticationFailed("此令牌对任何类型的令牌无效")

        # 检测token是否更新， 强制下线功能思路
        if not token or token != cache.get(token_cache_key(token)):
            raise AuthenticationFailed('此令牌已失效')

        validated_token = self.get_validated_token(token)

        return self.get_user(validated_token), validated_token

    @staticmethod
    def get_authorization(request: Request):
        authorization = request.headers.get('token')    # 请求头名字必须是 token
        if not authorization:
            raise AuthenticationFailed("login first!")

        authorization_list = authorization.split(" ")
        return authorization_list[0], authorization_list[1]

    def get_user(self, validated_token):

        try:
            user_id = validated_token['user_id']
        except KeyError:
            raise AuthenticationFailed("Token contained no recognizable user identification")

        try:
            user = Users.objects.get(pk=user_id)
        except self.user_model.DoesNotExist:
            raise AuthenticationFailed("User not found")

        if not user.is_active:
            raise AuthenticationFailed("your account is inactive", code='inactive')

        if api_settings.CHECK_REVOKE_TOKEN:
            if validated_token.get(
                    api_settings.REVOKE_TOKEN_CLAIM
            ) != get_md5_hash_password(user.password):
                raise AuthenticationFailed(
                    "The user's password has been changed.", code="password_changed"
                )

        return user
