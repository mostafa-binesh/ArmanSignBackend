from django.contrib.auth.models import User, Group
from rest_framework import serializers

from clients.serializers import ClientSerializer
from machines.serializers import MachineSerializer
from orders.serializers import OrderSerializer
from .models import Report
from clients.models import Client
from stages.models import Stage
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ReportSerializer(serializers.ModelSerializer):
    # read-only fields for get requests
    # client_detail = ClientSerializer(read_only=True)
    # creator = UserSer(read_only=True)
    # order_detail = OrderSerializer(read_only=True)
    # machine_detail = MachineSerializer(read_only=True)

    
    class Meta:
        model = Report
        fields = '__all__'