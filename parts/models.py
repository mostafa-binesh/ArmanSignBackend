from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Part(models.Model):
    title = models.CharField(max_length=200,verbose_name=_("Title"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    # updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Part")
        verbose_name_plural = _("Parts")

    def __str__(self) -> str:
        return self.title
