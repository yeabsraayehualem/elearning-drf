import datetime
from django.db import models
from administrators.models import Course
from users.models import User

# Create your models here.
class Submission(models.Model):
    assignment = models.ForeignKey("teachers.Assignment",  on_delete=models.CASCADE)
    student= models.ForeignKey("users.User", on_delete=models.CASCADE)
    grades= models.CharField(max_length=5)
    

    
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} {self.assignment.title.lesson_title}"


class Cart(models.Model):
    user= models.ForeignKey(to=User,on_delete=models.CASCADE)
    course= models.ForeignKey(to=Course,on_delete=models.CASCADE)
    startdate= models.DateField(auto_now_add=True)
    endDate=  models.DateField()

    
    def __str__(self):
        return f'{self.user}-{self.course}'
 