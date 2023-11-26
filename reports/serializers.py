from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ['title', 'creator', 'user', 'stage', 'started_at', 'ended_at', 'standard_time', 'intact_parts_count', 'defective_parts_count', 'stop_time']