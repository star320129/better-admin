from utils import NewResponse
from utils.common_mixins import *
from utils.common_jwt_authentication import NewJWTAuthentication
from . import models
from django.core.cache import cache
from .tools import UserPermission, ObtainSerializer, ButtonSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated


class PermissionView(
    GenericViewSet,
    NewListMixin,
    NewCreateMixin,
    NewUpdateMixin,
    NewDeleteMixin,
):
    authentication_classes = (NewJWTAuthentication,)
    permission_classes = (IsAuthenticated, UserPermission,)
    queryset = models.Permission.objects.filter(is_deleted=False, elem=0).all()
    serializer_class = ObtainSerializer

    def list(self, request, *args, **kwargs):

        res = super().list(request, *args, **kwargs)
        if res.data.get('result'):
            res.data['result'] = self.custom_dir(res.data.get('result'))
        return res

    @staticmethod
    def custom_dir(result):
        def clean_children(dic, depth=3):
            # 检查 'children' 是否存在且不为空，并且递归深度大于0
            if 'children' in dic and dic['children'] and depth > 0:
                # 清理 'children' 中的每个项，递归深度减1
                dic['children'] = [clean_children(child, depth - 1) for child in dic['children']]
            elif 'children' in dic:
                # 如果 'children' 为空或不存在，从字典中删除它
                del dic['children']

            return dic

        # 构建一个新列表
        new_result = []
        for item in result:
            new_result.append(clean_children(item))

        return new_result


class ButtonView(
    GenericViewSet,
    NewListMixin,
):
    authentication_classes = (NewJWTAuthentication,)
    permission_classes = (IsAuthenticated, UserPermission,)
    queryset = models.Permission.objects.filter(is_deleted=False, elem=3).all()
    serializer_class = ButtonSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data.get('result'):
            response.data['result'] = [{_['name']: _['path']} for _ in response.data['result']]
        return response
