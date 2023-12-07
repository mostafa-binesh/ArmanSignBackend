from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Order
from parts.serializers import PartSerializer
from clients.serializers import ClientSerializer

class OrderReadSerializer(serializers.ModelSerializer):
    parts = PartSerializer(many=True)
    client = ClientSerializer()
    class Meta:
        model = Order
        fields = '__all__'
class OrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'