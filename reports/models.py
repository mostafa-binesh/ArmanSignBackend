from django.db import models
from django.contrib.auth.models import User
from stages.models import Stage
from clients.models import Client
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"), default="")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Creator"), default=1) 
    user = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("User"))
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name=_("Stage"))
    started_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Started At"))
    ended_at = models.DateTimeField(verbose_name=_("Ended At"))
    standard_time = models.DateTimeField(verbose_name=_("Standard Time"))
    intact_parts_count = models.IntegerField(verbose_name=_("Intact Parts Count"))
    defective_parts_count = models.IntegerField(verbose_name=_("Defective Parts Count"))
    stop_time = models.IntegerField(verbose_name=_("Stop Time"))
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

    class Meta:
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")
        
    def __str__(self) -> str:
        return self.title