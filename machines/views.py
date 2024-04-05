from .serializers import MachineSerializer
from .models import Machine
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all().order_by('sort_order')  # Explicitly ordering by 'sort_order'
    serializer_class = MachineSerializer
    filter_backends = [DjangoFilterBackend]
    # permission_classes = [IsAdminUser]