from django.db import models
from django.utils.translation import gettext as _


class Stage(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    
    class Meta:
        verbose_name = _("Stage")
        verbose_name_plural = _("Stages")
        
    def __str__(self) -> str:
        return self.title