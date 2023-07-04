from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.IntegerField()
    address=models.CharField(max_length=500)