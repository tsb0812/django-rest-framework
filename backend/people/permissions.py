# We want only the user that created the people object to update and delete it.
# This can be achieved by using object level permissions

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.account == request.user
