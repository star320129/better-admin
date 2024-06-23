from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render
from django.contrib.auth.models import User
from .common_jwt_authentication import NewJWTAuthentication


class RouterPermissionMiddleware(MiddlewareMixin):

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """
        django 自带admin访问限制
        :param request:
        :param callback: 视图函数
        :param callback_args:
        :param callback_kwargs:
        :return:
        """
        if '/user/admin/' in request.path:
            tup = NewJWTAuthentication.authenticate(NewJWTAuthentication(), request)
            user = User.objects.filter(username=tup[0].username).first()
            if not user or not user.is_staff:
                return render(request, '404.html')

