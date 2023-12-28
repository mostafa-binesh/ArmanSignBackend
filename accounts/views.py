from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User

from accounts.serializers import OperatorFilterSerializer
# Create your views here.
class OperatorFilterListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = OperatorFilterSerializer