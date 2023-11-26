from rest_framework import viewsets
from .serializers import  ReportSerializer
from .models import Report
from rest_framework import viewsets
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    # permission_classes = [IsAdminUser]