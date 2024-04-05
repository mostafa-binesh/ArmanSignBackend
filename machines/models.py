from django.db import models
from django.utils.translation import gettext_lazy as _
class Machine(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    sort_order = models.PositiveIntegerField(default=1, blank=False, null=False,verbose_name=_("Sort Order"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _("Machine")
        verbose_name_plural = _("Machines")
        
    def __str__(self) -> str:
        return self.title