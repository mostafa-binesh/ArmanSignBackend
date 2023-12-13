from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Order
from parts.serializers import PartSerializer
from clients.serializers import ClientSerializer

class OrderReadSerializer(serializers.ModelSerializer):
    part = PartSerializer()
    client = ClientSerializer()
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)
class OrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_number','created_at', 'updated_at',)
