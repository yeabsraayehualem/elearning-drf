from django.shortcuts import render

from .utils import StaffPermissionClass


from .models import *
from .serializers import *
from rest_framework import generics, permissions,views,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
# TODO: create views to  to verify certificate.  needs to follow up students status. we do that from an exam
class ApproveCourses(views.APIView):
    permission_classes = []
    authentication_classes=[]

    def get(self, request, *args, **kwargs):
        token =request.headers.get("Authorization")
        if token:
            user = Token.objects.filter(key = token).first()
            user = user.user 
            
            if user.role == "Admin":
                
                course_id = self.kwargs.get('id')
            
                c_status = self.kwargs.get('status')
                print(course_id,c_status)
                
                try:
                    course = Course.objects.get(id=course_id)
                    course.status = c_status
                    course.save()
                    print(course.status)
                    return Response({'message': "Updated successfully"}, status=status.HTTP_200_OK)
                except Course.DoesNotExist:
                    return Response({'error': "Course not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error':'course update allowed for staff only'}, status= status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error':"User not identified"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class UpdateUser(views.APIView):
    permission_classes = []
    authentication_classes=[]

    def get(self, request, *args, **kwargs):
        token =request.headers.get("Authorization")
        if token:
            user = Token.objects.filter(key = token).first()
            user = user.user 
            print(user.role)
            if user.role == "Admin" and user.is_staff:
                
                user_id = self.kwargs.get('id')
            
                role= self.kwargs['role']
                
                try:
                    user = User.objects.get(id=user_id)
                    user.role = role
                    user.save()
                   
                    return Response({'message': "Updated successfully"}, status=status.HTTP_200_OK)
                except Course.DoesNotExist:
                    return Response({'error': "User not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error':'user update allowed for staff only'}, status= status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error':"User not identified"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)