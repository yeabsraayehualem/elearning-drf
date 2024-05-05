from django.db import models

from users.models import User

# Create your models here.
class Company(models.Model):
    name= models.CharField(max_length=100)
    landingDescription= models.TextField()
    goal= models.TextField()
    languagesQuealified= models.TextField()
    mentorsCallMessage= models.TextField()
    exploreEthiopiaText= models.TextField()
    sudentsNumber= models.IntegerField()
    
    def __str__(self):
        return f"{self.name} description"

class Languages(models.Model):
    language= models.CharField(max_length=120)
    
    
    def __str__(self):
        return self.language


class Course(models.Model):
    
    course_title= models.CharField(max_length=60)
    description= models.TextField()
    certification= models.BooleanField(default=False)
    expectedTrainee=models.CharField(max_length=60)
    price= models.CharField(max_length=10)
    duration= models.CharField(max_length=12)
   
    noOfLessons= models.IntegerField()
    noOfQuizes= models.IntegerField()
    teacher= models.ForeignKey(to=User, on_delete=models.CASCADE)
    status= models.CharField(choices=[(i,i) for i in ['pending','approved','declined']], max_length=40, default="pending")
    def __str__(self):
        return self.course_title
class BookType(models.Model):
    type = models.CharField(max_length=200, )
    

    
    def __str__(self):
        return self.type

class Books(models.Model):
    title= models.CharField(max_length=120)
    type= models.ForeignKey(to=BookType,  on_delete=models.CASCADE)
    price= models.CharField(max_length=10)
    numberOfPages= models.IntegerField()
    file= models.FileField( upload_to='books/')
    iconImage= models.ImageField(upload_to='bookIcon/')
    rating= models.CharField(max_length=10)
    uploadDate= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
 