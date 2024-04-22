from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('sort_order')  # Explicitly ordering by 'sort_order'
    serializer_class = ProjectSerializer
    # permission_classes = [IsAdminUser]
