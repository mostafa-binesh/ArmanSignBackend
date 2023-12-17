from rest_framework import viewsets
from .serializers import  ReportReadSerializer, ReportWriteSerializer
from .models import Report
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ReportFilter
from rest_framework import permissions
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
        
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReportFilter
    # permission_classes = [IsAdminUser]
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ReportWriteSerializer

        return ReportReadSerializer