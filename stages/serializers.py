from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Stage


class StageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stage
        fields = ['title']