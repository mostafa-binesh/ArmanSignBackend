from rest_framework import viewsets
from .serializers import PartSerializer
from .models import Part
from rest_framework import viewsets
class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    # permission_classes = [IsAdminUser]