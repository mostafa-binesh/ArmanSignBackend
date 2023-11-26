from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['parts', 'client', 'count', 'created_at', 'order_number']