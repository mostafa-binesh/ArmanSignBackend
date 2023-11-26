from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Part


class PartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Part
        fields = ['title']