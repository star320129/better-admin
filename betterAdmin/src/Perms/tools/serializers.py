from rest_framework import serializers
from .. import models


class ObtainSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Permission
        fields = '__all__'
