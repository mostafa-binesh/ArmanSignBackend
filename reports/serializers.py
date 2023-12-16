from django.contrib.auth.models import User, Group
from rest_framework import serializers

from clients.serializers import ClientSerializer
from orders.serializers import OrderReadSerializer
from machines.serializers import MachineSerializer
from clients.serializers import ClientSerializer
from machines.serializers import MachineSerializer
from accounts.serializers import OperatorSerializer
from .models import Report
from django.utils.translation import gettext_lazy as _

class ReportReadSerializer(serializers.ModelSerializer):
    order = OrderReadSerializer()
    # client = ClientSerializer()
    machine = MachineSerializer()
    operator = OperatorSerializer()
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)
class ReportWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)