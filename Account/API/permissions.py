from rest_framework import permissions
class AccountPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method==permissions.SAFE_METHODS:
            return True
        return obj.UserAccount.id==request.user.id