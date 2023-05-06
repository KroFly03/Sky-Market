from rest_framework.permissions import BasePermission

from users.models import UserRoles


class AdminRequired(BasePermission):
    message = 'You must be admin.'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.ADMIN:
            return True


class OwnerRequired(BasePermission):
    message = 'You must be owner.'

    def has_object_permission(self, request, view, obj):
        if obj.author.pk == request.user.pk:
            return True
