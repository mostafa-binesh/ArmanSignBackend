from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # todo
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    
    def __str__(self) -> str:
        return self.name