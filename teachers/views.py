import json
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import status
from users.models import User

from .models import Course, Lessons, Assignment
from .serializers import CourseSerializer, LessonsSerializer, AssignmentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import *
class CourseCreate(APIView):
    serializer_class = CourseSerializer
    authentication_classes=[]
    permission_classes=[]
    def post(self, request, format=None):
        token = self.request.headers.get('Authorization')
        user = Token.objects.filter(key=token).first()
        
        if user:
            role = user.user.role
            if role == "Teacher":
                # Deserialize request data
                serializer = self.serializer_class(data=request.data)
                
                # Validate and save the serializer
                if serializer.is_valid():
                    course=  serializer.save(teacher= User.objects.get(id=4))
                  
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Return forbidden if user is not a teacher
                return Response({"error": "Only teachers can create courses"}, status=status.HTTP_403_FORBIDDEN)
        else:
            # Return unauthorized if token is not valid
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

class LessonCreate(CreateAPIView):
    queryset = Lessons.objects.all()  # Optionally, specify queryset if needed
    serializer_class = LessonsSerializer
    permission_classes=[]
    authentication_classes=[]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class GetMyCourses(APIView):
    serializer_class = CourseSerializer
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')
        user_token = Token.objects.filter(key=token).first()

        if user_token:
            role = user_token.user.role
            if role == "Teacher":
                courses = Course.objects.filter(teacher=user_token.user)
                serializer = self.serializer_class(courses, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Only teachers have courses."}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Invalid token."}, status=status.HTTP_401_UNAUTHORIZED)
                
# TODO: create exam model and a way to make the users take exams, if they score more than the pass point allow certificatio to them
# TODO: here is how it happens, if they get more that the pass point their acc ll be sent for the admin s to b certified. then they get their certification through their email. 
