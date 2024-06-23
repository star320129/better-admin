from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or view.action == 'list':
            return True

    def has_object_permission(self, request, view, obj):
        self.has_permission(request, view)
