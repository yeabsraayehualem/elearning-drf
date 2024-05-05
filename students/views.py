from django.shortcuts import render

from teachers.models import Lessons
from .serializers import *
from .models import *
from rest_framework import generics,views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import status



class SubmitAssignment(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
 
class EnroleToCourse(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CartSerializer
    # parser_classes = [FileUploadParser]

    def post(self, request, format=None):
        token = request.headers.get('Authorization')
        user_token = Token.objects.filter(key=token).first()
        
        if user_token:
            role = user_token.user.role
            if role == "Student":
                print("Request Data:", request.data)  
                serializer = self.serializer_class(data=request.data)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Only teachers can create lessons"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        

class GetCourseVideos(views.APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')
        
        user_token = Token.objects.filter(key=token).first()
        
        if user_token:
            role = user_token.user.role
            if role == "Student":
                user = user_token.user
                course = Cart.objects.filter(user=user, course__id=self.kwargs['course_id']).first()
                
                if course:
                    lessons = Lessons.objects.filter(course__id=self.kwargs['course_id'])
                    serializer = GetLessonsSerializer(lessons, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"error": "Only students can access course videos"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)