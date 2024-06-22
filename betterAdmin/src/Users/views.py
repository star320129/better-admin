from utils import NewResponse
from utils.common_jwt_authentication import NewJWTAuthentication
from utils.common_mixins import *
from . import models
from .tools import LoginSerializer, UserSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class LoginView(GenericViewSet):

    serializer_class = LoginSerializer

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return NewResponse(message='login success!', result=serializer.validated_data)


class UserView(
    GenericViewSet,
    NewListMixin,
):
    authentication_classes = (NewJWTAuthentication, )
    permission_classes = (IsAuthenticated,)

    serializer_class = UserSerializer
    queryset = models.Users.objects.all()

