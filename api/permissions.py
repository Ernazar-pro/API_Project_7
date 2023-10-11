from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'POST', 'DELETE']:
            return request.user.is_staff


class CreatePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method  == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated

class CreateDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated