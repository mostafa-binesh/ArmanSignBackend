from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Order
from clients.models import Client

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    class Meta:
        model = Order
        fields = ['parts', 'client', 'count', 'started_at','ended_at', 'order_number']