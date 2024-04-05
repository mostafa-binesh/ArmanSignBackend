from django.db import models
from django.utils.translation import gettext_lazy as _
from pytz import timezone
# Create your models here.
class Client(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User")) # todo
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    phone_number = models.CharField(max_length=200, verbose_name=_("Phone Number"), null=True)
    email = models.EmailField(max_length=200, null=True, verbose_name=_("Email"))
    sort_order = models.PositiveIntegerField(default=1, blank=False, null=False,verbose_name=_("Sort Order"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
        ordering = ['sort_order']
    
    def __str__(self) -> str:
        return self.title