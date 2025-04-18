from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request):
        return request.user.is_authenticated and request.user.role == 'admin'
 
class IsUser(permissions.BasePermission):
    """
    Allows access only to Users users.
    """
    def has_permission(self, request):
        return request.user.is_authenticated and request.user.role == 'user'
 

 
class AdminFullUserReadOnly(permissions.BasePermission):
    """
    Allows full access to admin users and read-only access to interviewer users.
    """
    def has_permission(self, request):
        if not request.user.is_authenticated:
            return False
         
        if request.user.role == 'admin':
            return True
             
        if request.user.role == 'users' and request.method in permissions.SAFE_METHODS:
            return True
             
        return False 