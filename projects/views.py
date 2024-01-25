from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAdminUser]