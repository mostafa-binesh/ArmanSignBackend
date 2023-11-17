from django.db import models


class Stage(models.Model):
    title = models.CharField(max_length=200)