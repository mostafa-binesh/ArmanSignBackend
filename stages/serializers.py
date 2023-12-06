from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Stage


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['title']