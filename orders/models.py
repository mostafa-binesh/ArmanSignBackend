# Create your models here.
from django.db import models
from datetime import datetime    
from parts.models import Part
from clients.models import Client
# Create your models here.
class Order(models.Model):
    parts = models.ManyToManyField(Part)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now())
    order_number = models.CharField(max_length=200)
