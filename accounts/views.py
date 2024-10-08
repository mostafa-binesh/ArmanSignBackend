from telnetlib import STATUS
from django.conf import settings
from django.shortcuts import render
from rest_framework.generics import ListAPIView
# from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import OperatorFilterSerializer, UserSerializer, SignupSerializer


# Create your views here.
class OperatorFilterListView(ListAPIView):
    queryset = User.objects.filter(groups__name="Operator")
    serializer_class = OperatorFilterSerializer


class OperatorAndSupervisorFilterListView(ListAPIView):
    # Define the list of group names you're interested in
    group_names = ["Operator", "Supervisor"]

    # Queryset to find users belonging to either "Operator" or "Supervisor" groups
    queryset = User.objects.filter(groups__name__in=group_names).distinct()
    queryset = User.objects.filter(groups__name="Operator")
    serializer_class = OperatorFilterSerializer


class UserInfoListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer

    def get_queryset(self):
        # Filter the queryset to only include the authenticated user
        user = self.request.user
        return User.objects.filter(id=user.id)


class UserGroupsoListView(APIView):
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer

    def get(self, request):
        groups = request.user.groups.all()
        groupNames = [group.name for group in groups]
        return Response(groupNames, status=200)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_backends = [DjangoFilterBackend]
    # permission_classes = [IsAdminUser]


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
