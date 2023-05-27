from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser  
class User(AbstractUser):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name', 'password']


class Book(models.Model):
    title= models.CharField(max_length=100)
    no_of_pages=models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()


    def __str__(self) -> str:
        return self.title
