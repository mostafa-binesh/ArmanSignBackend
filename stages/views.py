from rest_framework import viewsets
from .serializers import StageSerializer
from .models import Stage
from rest_framework import viewsets
class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    # permission_classes = [IsAdminUser]