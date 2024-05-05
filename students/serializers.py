from teachers.models import Lessons
from .models import *
from rest_framework import serializers

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Submission
        fields = '__all__'
        

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields=['user','course','endDate']
        
class GetLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Lessons
        fields = ['course','lesson_title','description','video_file']