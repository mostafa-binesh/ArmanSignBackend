# Create your models here.
from django.db import models
from datetime import datetime
from projects.models import Project    
from parts.models import Part
from clients.models import Client
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import random
# Create your models here.
class Order(models.Model):
    CATEGORY_CHOICES = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ]
    part = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name=_("Part"))
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("Client"))
    count = models.IntegerField(default=0, verbose_name=_("Count"))
    started_at = models.DateField(default=timezone.now, verbose_name=_("Started At"))
    ended_at = models.DateField(default=timezone.now, verbose_name=_("Ended At"), null=True)
    order_number = models.CharField(max_length=200, verbose_name=_("Order Number"))

    project = models.ForeignKey(Project,on_delete=models.CASCADE, verbose_name=_('Project'), default=1)
    category = models.CharField(verbose_name=_("Category"), max_length=20,  choices=CATEGORY_CHOICES, default='a')

    sort_order = models.PositiveIntegerField(default=1, blank=False, null=False,verbose_name=_("Sort Order"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        
    def __str__(self) -> str:
        return self.order_number
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super(Order, self).save(*args, **kwargs)

    def _generate_order_number(self) -> str:
        if not self.order_number:
            # Get first three digits of client_id
            client_id_str = '{:03d}'.format(self.client.id)[:3]

            # Get first three digits of part_id
            part_id_str = '{:03d}'.format(self.part.id)[:3]

            # Calculate the order count for the client and format it as three digits
            order_count = Order.objects.filter(client=self.client).count()
            order_count_str = '{:03d}'.format(order_count + 1)  # Add 1 as we're creating a new order

            # Combine all parts to form the order_number
            return '{}{}{}'.format(client_id_str, part_id_str, order_count_str)