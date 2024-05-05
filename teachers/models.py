from django.db import models
from administrators.models import Books, Course

from users.models import User

# Create your models here.


class Lessons(models.Model):
    lesson_title= models.CharField(max_length=60)
    description= models.TextField()
   
    video_file = models.FileField(upload_to='videos/', null=True)
    course= models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lesson_title}"
    
class Assignment(models.Model):
    course= models.ForeignKey(to=Course, on_delete=models.CASCADE)
    title= models.ForeignKey(to=Lessons, on_delete=models.CASCADE)
    description= models.TextField()
    grade= models.CharField(max_length=10)


    def __str__(self):
        return f"{self.course.course_title}-{self.title.lesson_title}"


