from random import choice
from django.db import models
from django.contrib.auth.models import User
from orders.models import Order
from stages.models import Stage
from clients.models import Client
from machines.models import Machine
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Report(models.Model):
    STATUS_CHOICES = [
        ('p', 'Pending'),
        ('a', 'Approved'),
        ('r', 'Rejected'),
    ]
    
    
    # title = models.CharField(max_length=200, verbose_name=_("Title"))
    operator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Operator")) 
    # client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("Client"))
    order = models.ForeignKey(Order,on_delete=models.CASCADE, verbose_name=_('Order'))
    machine = models.ForeignKey(Machine,on_delete=models.CASCADE, verbose_name=_('Machine'))
    started_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Started At"))
    ended_at = models.DateTimeField(verbose_name=_("Ended At"), null=True)
    standard_time = models.IntegerField(verbose_name=_("Standard Time"))
    intact_parts_count = models.IntegerField(verbose_name=_("Intact Parts Count"))
    defective_parts_count = models.IntegerField(verbose_name=_("Defective Parts Count"))
    # stop_time = models.In tegerField(verbose_name=_("Stop Time"))
    status = models.CharField(verbose_name=_("Status"), max_length=20,  choices=STATUS_CHOICES, default='p')
    # i didn't like this style of stop controller code and time, but this project doesn't need more than this
    # and more modular and flexible design is more time consuming
    stop_controller_1_code = models.CharField(max_length=10, blank=True, null=True)
    stop_controller_1_time = models.IntegerField(blank=True, null=True)

    stop_controller_2_code = models.CharField(max_length=10, blank=True, null=True)
    stop_controller_2_time = models.IntegerField(blank=True, null=True)

    stop_controller_3_code = models.CharField(max_length=10, blank=True, null=True)
    stop_controller_3_time = models.IntegerField(blank=True, null=True)

    stop_controller_4_code = models.CharField(max_length=10, blank=True, null=True)
    stop_controller_4_time = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")
        
    def __str__(self) -> str:
        return self.title