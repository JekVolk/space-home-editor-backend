from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.models import Project, SettingsSpaceStation
from project.serializers import ProjectSerializer, SettingsSerializer
from space_home_editor.utils import path_params


# -------------------------- Project ------------------------------------------
@path_params("id")
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=True, methods=["get", "put", "patch"], url_path="settings")
    def settings(self, request, pk=None):
        project = self.get_object()
        try:
            settings = project.settings
        except SettingsSpaceStation.DoesNotExist:
            # якщо не існує – створимо за замовчуванням
            settings = SettingsSpaceStation.objects.create(project=project)

        if request.method == "GET":
            serializer = SettingsSerializer(settings)
            return Response(serializer.data)

        if request.method in ["PUT", "PATCH"]:
            serializer = SettingsSerializer(settings, data=request.data, partial=(request.method=="PATCH"))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)