from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True
