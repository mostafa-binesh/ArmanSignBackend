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
from django.utils.translation import gettext_lazy as _
class ReportPartCodesSerializer(serializers.ModelSerializer):
    # started_at = serializers.TimeField(format='%H:%M:%S')
    # ended_at = serializers.TimeField(format='%H:%M:%S')

    class Meta:
        model = Report_Parts_Code
        fields = ['number']
        read_only_fields = ('created_at', 'updated_at',)
        
class ReportReadSerializer(serializers.ModelSerializer):
    order = OrderReadSerializer()
    # client = ClientSerializer()
    machine = MachineSerializer()
    operator = OperatorSerializer()
    # project = ProjectSerializer()
    parts = PartSerializer(many=True)
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
    # report_part_codes = ReportPartCodesSerializer(many=True)
    # report_part_codes = serializers.SerializerMethodField()  # Serializer method field to handle related Report_Parts_Code
    # report_part_codes = serializers.PrimaryKeyRelatedField(queryset=Report_Parts_Code.objects.all(), many=True)


    # def create(self, validated_data):
        # part_codes_data = validated_data.pop('report_part_codes', [])
        # report_parts = validated_data.pop('parts', [])
        # report = Report.objects.create(**validated_data)
        # report.report_part_codes.set(part_codes_data)
        # report.parts.set(report_parts)
        # for part_code_data in part_codes_data:
        #     Report_Parts_Code.objects.create(report=report, **part_code_data)
        # return report
    # def create(self, validated_data):
    #     report_part_codes_data = validated_data.pop('report_part_codes', [])
    #     # report_part_codes_data = validated_data.pop('parts', [])
    #     report = Report.objects.create(**validated_data)

    #     # Handle many-to-many relationship
    #     report_part_codes = []
    #     for part_code_id in report_part_codes_data:
    #         part_code = Report_Parts_Code.objects.create(report=report, number=part_code_id)
    #         report_part_codes.append(part_code)

    #     return report
    def get_report_part_codes(self, obj):
        report_part_codes = Report_Parts_Code.objects.filter(report=obj)
        return ReportPartCodesSerializer(report_part_codes, many=True).data

    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)
    
