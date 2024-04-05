from rest_framework import viewsets
from .serializers import  ReportReadSerializer, ReportWriteSerializer
from .models import Report
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ReportFilter
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
import csv
from django.http import HttpResponse

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('sort_order')  # Explicitly ordering by 'sort_order'
        
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReportFilter
    # permission_classes = [IsAdminUser]
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ReportWriteSerializer

        return ReportReadSerializer
    
class ReportExportView(ListAPIView):
    serializer_class = ReportReadSerializer
    queryset = Report.objects.all().order_by('sort_order')  # Explicitly ordering by 'sort_order'
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReportFilter
    # filterset_fields = ['status', 'operator', 'machine']  # Add any other fields you want to filter by
    # search_fields = ['order__name', 'machine__name']
    # ordering_fields = '__all__'

    def get(self, request, *args, **kwargs):
        response_format = request.query_params.get('format', 'csv')  # or use request.GET
        if response_format.lower() == 'csv':
            return self.export_as_csv()
        else:
            return super().get(request, *args, **kwargs)

    def export_as_csv(self):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="report.csv"'
        
        writer = csv.writer(response)
        print(queryset)  # Will display QuerySet in the console
        print(serializer.data)  # Will display serializer data which is about to be written to CSV
        # Write your headers first
        writer.writerow(serializer.data[0].keys())
        # tranlate headers
        for item in serializer.data:
            writer.writerow([
                item['id'], 
                item['order']['order_number'],
                item['machine']['title'],
                item['operator']['username'],
                item['date'],
                item['started_at'],
                item['ended_at'],
                item['standard_time'],
                item['intact_parts_count'],
                item['defective_parts_count'],
                item['status'],
                item['stop_controller_1_code'],
                item['stop_controller_1_time'],
                item['stop_controller_2_code'],
                item['stop_controller_2_time'],
                item['stop_controller_3_code'],
                item['stop_controller_3_time'],
                item['stop_controller_4_code'],
                item['stop_controller_4_time'],
                item['created_at'],
                item['updated_at'],
            ])
        
        return response