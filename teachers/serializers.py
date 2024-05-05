from .models import *
from rest_framework import serializers

from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_title', 'description', 'certification', 'expectedTrainee', 'price', 'duration', 'noOfLessons', 'noOfQuizes']

        

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Lessons
        fields = ['lesson_title','description','course','video_file']
    video_file = serializers.FileField()
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Assignment
        fields = '__all__'       
        