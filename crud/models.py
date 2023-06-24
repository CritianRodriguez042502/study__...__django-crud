from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Taks (models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    creation = models.DateTimeField(auto_now_add= True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return f"Taks: {self.title}"
    
    
    
class User_registration (models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(null=False, max_length=150)
    password_1 = models.CharField(max_length=30)
    password_2 = models.CharField(max_length=30)