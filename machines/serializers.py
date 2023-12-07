from rest_framework import serializers
from .models import Machine
from django.utils.translation import gettext_lazy as _

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'title']