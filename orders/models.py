# Create your models here.
from django.db import models
from datetime import datetime    
from parts.models import Part
from clients.models import Client
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.
class Order(models.Model):
    parts = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name=_("Part"))
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("Client"))
    count = models.IntegerField(default=0, verbose_name=_("Count"))
    started_at = models.DateField(default=timezone.now, verbose_name=_("Started At"))
    ended_at = models.DateField(default=timezone.now, verbose_name=_("Ended At"), null=True)
    order_number = models.CharField(max_length=200, verbose_name=_("Order Number"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        
    def __str__(self) -> str:
        return self.order_number