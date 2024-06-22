from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.utils import get_md5_hash_password

from src.Users.models import Users


class NewJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        header, token = self.get_authorization(request)
        assert header and header == 'Bearer', "此令牌对任何类型的令牌无效"

        validated_token = self.get_validated_token(token)

        return self.get_user(validated_token), validated_token

    @staticmethod
    def get_authorization(request: Request):
        authorization = request.headers.get('token')
        assert authorization, "login first!"
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
