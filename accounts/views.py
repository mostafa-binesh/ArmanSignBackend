from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from accounts.serializers import OperatorFilterSerializer, UserSerializer
# Create your views here.
class OperatorFilterListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = OperatorFilterSerializer
class OperatorFilterListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_backends = [DjangoFilterBackend]
    # permission_classes = [IsAdminUser]