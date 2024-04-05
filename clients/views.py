from django.shortcuts import render
from rest_framework import viewsets
from .models import Client

from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('sort_order')  # Explicitly ordering by 'sort_order'
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated]