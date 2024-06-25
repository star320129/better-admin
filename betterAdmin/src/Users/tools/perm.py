from rest_framework.permissions import BasePermission
from utils.common_function import permissions_user


class AdminPermission(BasePermission):

    prefix_action = 'user:action'
    prefix_posts = 'user:posts'
    prefix_online = 'user:online'
    permissions = None

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        self.permissions = permissions_user(request.user)
        if any((
            ':'.join((self.prefix_action, view.action)) in self.permissions,
            ':'.join((self.prefix_posts, view.action)) in self.permissions,
            ':'.join((self.prefix_online, view.action)) in self.permissions
        )):
            return True

    def has_object_permission(self, request, view, obj):
        self.has_permission(request, view)

