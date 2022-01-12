from rest_framework import permissions


class CustomePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1