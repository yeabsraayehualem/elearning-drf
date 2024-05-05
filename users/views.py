from django.shortcuts import render

from administrators.models import Course
from administrators.serializers import CourseSerializer
from .models import *
from .serializers import *
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = (permissions.AllowAny,)



class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(email=email, password=password)

        if user:
            # Generate or retrieve authentication token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, "user_id": user.id, "role": user.role}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class GetAllCourses(generics.ListAPIView):
    serializer_class= CourseSerializer
    queryset= Course.objects.all()
    permission_classes = (permissions.AllowAny,)
