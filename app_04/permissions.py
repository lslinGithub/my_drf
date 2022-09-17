from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # 这个是是否有修改权限的
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

    # 是否有获取权限
    def has_permission(self, request, view):
        # do something
        return True
