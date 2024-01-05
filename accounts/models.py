from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # add your additional fields here
    national_code = models.CharField(max_length=30)