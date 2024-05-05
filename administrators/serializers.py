from rest_framework import serializers
from .models import *



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields = '__all__'
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model= Company
        fields = '__all__'

class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Languages
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields = '__all__'
class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookType
        fields = '__all__'
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model= Books
        fields = '__all__'

# class PackageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Package
#         fields = '__all__'
  
  