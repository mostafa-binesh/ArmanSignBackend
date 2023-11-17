from django.db import models

# Create your models here.
class Part(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField("created_at", auto_now_add=True)

    def __str__(self) -> str:
        return self.title
