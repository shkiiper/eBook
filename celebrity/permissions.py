from rest_framework import permissions


class IsReadOnly(permissions.BasePermission):
    """
    Разрешить только чтение (GET, HEAD, OPTIONS) для всех пользователей.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
