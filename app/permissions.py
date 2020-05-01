from rest_framework import permissions

"""
For authentication use built-in permission classes: 
IsAuthenticated, IsAuthenticatedOrReadOnly etc.
https://www.django-rest-framework.org/api-guide/permissions/
"""


class IsOwner(permissions.BasePermission):
    """Permission for object owner"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission for Admin to use all methods.
    Read only allowed for other users.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  #
            return True
        else:
            return request.user.is_staff
