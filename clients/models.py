from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Client(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User")) # todo
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    phone_number = models.CharField(max_length=200, verbose_name=_("Phone Number"))
    email = models.EmailField(max_length=200, null=True, verbose_name=_("Email"))
    
    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
    
    def __str__(self) -> str:
        return self.name