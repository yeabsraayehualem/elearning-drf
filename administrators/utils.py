from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission


class StaffPermissionClass(BasePermission):
   

    def has_permission(self, request, view):
        
        token =request.headers.get("Authorization")
        if token:
            user = Token.objects.filter(key = token).first()
            user = user.user 
            if user.role == "Staff" and user.is_staff:
                return True
            return False
        
        return False