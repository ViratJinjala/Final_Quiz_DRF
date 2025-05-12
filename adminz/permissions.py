from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin == True
 
class IsUser(permissions.BasePermission):
    """
    Allows access only to Users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin == False
 

 
class AdminFullUserReadOnly(permissions.BasePermission):
    """
    Allows full access to admin users and read-only access to interviewer users.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
         
        if request.user.is_admin == True:
            return True
             
        if request.user.is_admin == False and request.method in permissions.SAFE_METHODS:
            return True
             
        return False 