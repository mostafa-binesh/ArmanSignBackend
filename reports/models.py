from django.db import models
from django.contrib.auth.models import User
from stages.models import Stage
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User")) # todo
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name=_("Stage"))
    started_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Started At"))
    ended_at = models.DateTimeField(verbose_name=_("Ended At"))
    standard_time = models.DateTimeField(verbose_name=_("Standard Time"))
    intact_parts_count = models.IntegerField(verbose_name=_("Intact Parts Count"))
    defective_parts_count = models.IntegerField(verbose_name=_("Defective Parts Count"))
    stop_time = models.IntegerField(verbose_name=_("Stop Time"))

    class Meta:
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")