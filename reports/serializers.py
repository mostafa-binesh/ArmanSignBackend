from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Report
from clients.models import Client
from stages.models import Stage
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
                'title', 'creator', 'user', 'stage', 'started_at', 'ended_at', 'standard_time',
                  'intact_parts_count', 'defective_parts_count', 'stop_time',
                  'stop_controller_1_code', 'stop_controller_2_code','stop_controller_3_code','stop_controller_4_code',
                  'stop_controller_1_time', 'stop_controller_2_time','stop_controller_3_time', 'stop_controller_4_time',
                  ]