from django.db import models
from django.contrib.auth.models import User
from stages.models import Stage
# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # todo
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField()
    standard_time = models.DateTimeField()
    intact_parts_count = models.IntegerField()
    defective_parts_count = models.IntegerField()
    stop_time = models.IntegerField()