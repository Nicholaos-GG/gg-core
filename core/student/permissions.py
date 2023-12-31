from rest_framework.permissions import BasePermission


class IsAdminUserorAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return bool(request.user and request.user.is_staff)
