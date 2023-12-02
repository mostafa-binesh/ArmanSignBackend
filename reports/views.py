from rest_framework import viewsets
from .serializers import  ReportSerializer
from .models import Report
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ReportFilter
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReportFilter
    # permission_classes = [IsAdminUser]