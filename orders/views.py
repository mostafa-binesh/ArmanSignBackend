from rest_framework import viewsets
from .serializers import OrderWriteSerializer, OrderReadSerializer
from .models import Order
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OrderFilter
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter
    # permission_classes = [IsAdminUser]
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return OrderWriteSerializer

        return OrderReadSerializer