from rest_framework.permissions import BasePermission
from rest_framework import permissions
class ProductPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method==permissions.SAFE_METHODS:
            return True
        return True

