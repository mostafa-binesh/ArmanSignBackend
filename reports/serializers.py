from doctest import Example
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from clients.serializers import ClientSerializer
from projects.serializers import ProjectSerializer
from orders.serializers import OrderReadSerializer
from machines.serializers import MachineSerializer
from clients.serializers import ClientSerializer
from machines.serializers import MachineSerializer
from accounts.serializers import OperatorSerializer
from parts.serializers import PartSerializer
from .models import Report, Report_Parts_Code
from parts.models import Part
from django.utils.translation import gettext_lazy as _
class ReportPartCodesSerializer(serializers.ModelSerializer):
    # started_at = serializers.TimeField(format='%H:%M:%S')
    # ended_at = serializers.TimeField(format='%H:%M:%S')

    class Meta:
        model = Report_Parts_Code
        fields = ['number']
        # read_only_fields = ('created_at', 'updated_at',)
        
class ReportReadSerializer(serializers.ModelSerializer):
    order = OrderReadSerializer()
    # client = ClientSerializer()
    machine = MachineSerializer()
    operator = OperatorSerializer()
    # project = ProjectSerializer()
    part = PartSerializer()
    # report_part_codes = ReportPartCodesSerializer(many=True)
    report_part_codes = serializers.SerializerMethodField()  # Serializer method field to handle related Report_Parts_Code
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)
    def get_report_part_codes(self, obj):
        report_part_codes = Report_Parts_Code.objects.filter(report=obj)
        return ReportPartCodesSerializer(report_part_codes, many=True).data
class ReportWriteSerializer(serializers.ModelSerializer):
    started_at = serializers.TimeField(format='%H:%M:%S')
    ended_at = serializers.TimeField(format='%H:%M:%S')
    report_part_codes = ReportPartCodesSerializer(many=True, required=False)

    def create(self, validated_data):
        report_codes_data = validated_data.pop('report_part_codes', None)  # Pop the report_part_codes data or set it to None if not provided
        report = Report.objects.create(**validated_data)

        if report_codes_data:
            for report_code_data in report_codes_data:
                Report_Parts_Code.objects.create(report=report, **report_code_data)

        return report

    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)