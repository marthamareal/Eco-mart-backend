from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Allows only owners of an object or admins to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to owners and admins
        # Write permissions are only allowed to the owner of the object or admins
        return obj == request.user or request.user.is_superuser


class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
