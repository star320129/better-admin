from utils import NewResponse
from utils.common_mixins import *
from utils.common_jwt_authentication import NewJWTAuthentication
from . import models
from .tools import UserPermission, ObtainSerializer
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
    queryset = models.Permission.objects.filter(is_deleted=False).all()
    serializer_class = ObtainSerializer
