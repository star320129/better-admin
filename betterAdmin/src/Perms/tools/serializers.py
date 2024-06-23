from rest_framework import serializers
from .. import models


class ObtainSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Permission
        fields = ('id', 'name', 'path', 'icon', 'children')

    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, obj):
        return ObtainSerializer(obj.child.all(), many=True).data


class ButtonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Permission
        fields = ('name', 'path')

