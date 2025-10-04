from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.models import Project, SettingsSpaceStation, Module, ValueResourceModule, ExternalSystems, \
    ValueResourceExternalSystem, Compartment, ValueResourceCompartment, Zone, ValueResourceZone, Component, \
    ValueResourceComponent, Closet, ValueResourceCloset, InnerComponent, ValueResourceInnerComponent, Mission
from project.serializers import ProjectSerializer, SettingsSerializer, ModuleSerializer, ValueResourceModuleSerializer, \
    ExternalSystemsSerializer, ValueResourceExternalSystemSerializer, CompartmentSerializer, \
    ValueResourceCompartmentSerializer, ZoneSerializer, ValueResourceZoneSerializer, ComponentSerializer, \
    ValueResourceComponentSerializer, ClosetSerializer, ValueResourceClosetSerializer, InnerComponentSerializer, \
    ValueResourceInnerComponentSerializer, MissionsSerializer
from space_home_editor.utils import path_params


# -------------------------- Project ------------------------------------------
@path_params()
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @extend_schema(
        methods=["GET"],
        responses=SettingsSerializer,
        description="Отримати налаштування станції"
    )
    @extend_schema(
        methods=["PUT", "PATCH"],
        request=SettingsSerializer,
        responses=SettingsSerializer,
        description="Оновити налаштування станції"
    )
    @action(detail=True, methods=["get", "put", "patch"], url_path="settings")
    def settings_view(self, request, pk=None):
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

# -------------------------- Module ------------------------------------------

@path_params("project_pk")
class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        return Module.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        serializer.save(project_id=project_id)

@path_params("project_pk", "module_pk")
class ValueResourceModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ValueResourceModuleSerializer

    def get_queryset(self):
        return ValueResourceModule.objects.filter(module_id=self.kwargs["module_pk"])

    def perform_create(self, serializer):
        serializer.save(module_id=self.kwargs["module_pk"])

# -------------------------- ExternalSystems ------------------------------------------

@path_params("project_pk")
class ExternalSystemsViewSet(viewsets.ModelViewSet):
    serializer_class = ExternalSystemsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        return ExternalSystems.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        serializer.save(project_id=project_id)

@path_params("project_pk", "external_system_pk")
class ValueResourceExternalSystemViewSet(viewsets.ModelViewSet):
    serializer_class = ValueResourceExternalSystemSerializer

    def get_queryset(self):
        return ValueResourceExternalSystem.objects.filter(external_system_id=self.kwargs["external_system_pk"])

    def perform_create(self, serializer):
        serializer.save(external_system_id=self.kwargs["external_system_pk"])

# -------------------------- Compartment ------------------------------------------

@path_params("project_pk", "module_pk")
class CompartmentViewSet(viewsets.ModelViewSet):
    serializer_class = CompartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        return Compartment.objects.filter(project_id=project_id, module_id=module_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        serializer.save(project_id=project_id, module_id=module_id)

@path_params("project_pk", "module_pk", "compartment_pk")
class ValueResourceCompartmentViewSet(viewsets.ModelViewSet):
    serializer_class = ValueResourceCompartmentSerializer

    def get_queryset(self):
        return ValueResourceCompartment.objects.filter(compartment_id=self.kwargs["compartment_pk"])

    def perform_create(self, serializer):
        serializer.save(compartment_id=self.kwargs["compartment_pk"])

# -------------------------- Zone ------------------------------------------

@path_params("project_pk", "module_pk", "compartment_pk")
class ZoneViewSet(viewsets.ModelViewSet):
    serializer_class = ZoneSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        compartment_id = self.kwargs.get('compartment_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        if not compartment_id:
            raise ValidationError("Compartment ID is required")
        return Zone.objects.filter(project_id=project_id, compartment_id=compartment_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        compartment_id = self.kwargs.get('compartment_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        if not compartment_id:
            raise ValidationError("Compartment ID is required")
        serializer.save(project_id=project_id, compartment_id=compartment_id)

@path_params("project_pk", "module_pk", "compartment_pk", "zone_pk")
class ValueResourceZoneViewSet(viewsets.ModelViewSet):
    serializer_class = ValueResourceZoneSerializer

    def get_queryset(self):
        return ValueResourceZone.objects.filter(zone_id=self.kwargs["zone_pk"])

    def perform_create(self, serializer):
        serializer.save(zone_id=self.kwargs["zone_pk"])

# -------------------------- Component ------------------------------------------

@path_params("project_pk", "module_pk", "compartment_pk", "zone_pk")
class ComponentViewSet(viewsets.ModelViewSet):
    serializer_class = ComponentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        compartment_id = self.kwargs.get('compartment_pk')
        zone_id = self.kwargs.get('zone_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        if not compartment_id:
            raise ValidationError("Compartment ID is required")
        if not zone_id:
            raise ValidationError("Zone ID is required")
        return Component.objects.filter(project_id=project_id, zone_id=zone_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        compartment_id = self.kwargs.get('compartment_pk')
        zone_id = self.kwargs.get('zone_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        if not compartment_id:
            raise ValidationError("Compartment ID is required")
        if not zone_id:
            raise ValidationError("Zone ID is required")
        serializer.save(project_id=project_id, zone_id=zone_id)

@path_params("project_pk", "module_pk", "compartment_pk", "zone_pk", "components_pk")
class ValueResourceComponentViewSet(viewsets.ModelViewSet):
    serializer_class = ValueResourceComponentSerializer

    def get_queryset(self):
        return ValueResourceComponent.objects.filter(component_id=self.kwargs["component_pk"])

    def perform_create(self, serializer):
        serializer.save(component_id=self.kwargs["component_pk"])


# -------------------------- Closet ------------------------------------------


@path_params("project_pk", "module_pk", "compartment_pk", "zone_pk")
class ClosetViewSet(viewsets.ModelViewSet):
    serializer_class = ClosetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        compartment_id = self.kwargs.get('compartment_pk')
        zone_id = self.kwargs.get('zone_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        if not compartment_id:
            raise ValidationError("Compartment ID is required")
        if not zone_id:
            raise ValidationError("Zone ID is required")
        return Closet.objects.filter(project_id=project_id, zone_id=zone_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        compartment_id = self.kwargs.get('compartment_pk')
        zone_id = self.kwargs.get('zone_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        if not compartment_id:
            raise ValidationError("Compartment ID is required")
        if not zone_id:
            raise ValidationError("Zone ID is required")
        serializer.save(project_id=project_id, zone_id=zone_id)

@path_params("project_pk", "module_pk", "compartment_pk", "zone_pk", "closet_pk")
class ValueResourceClosetViewSet(viewsets.ModelViewSet):
    serializer_class = ValueResourceClosetSerializer

    def get_queryset(self):
        return ValueResourceCloset.objects.filter(closet_id=self.kwargs["closet_pk"])

    def perform_create(self, serializer):
        serializer.save(closet_id=self.kwargs["closet_pk"])

# -------------------------- InnerComponent ------------------------------------------


@path_params("project_pk", "module_pk", "compartment_pk", "zone_pk", "closet_pk")
class InnerComponentViewSet(viewsets.ModelViewSet):
    serializer_class = InnerComponentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        compartment_id = self.kwargs.get('compartment_pk')
        zone_id = self.kwargs.get('zone_pk')
        closet_id = self.kwargs.get('closet_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        if not compartment_id:
            raise ValidationError("Compartment ID is required")
        if not zone_id:
            raise ValidationError("Zone ID is required")
        if not closet_id:
            raise ValidationError("Closet ID is required")
        return InnerComponent.objects.filter(project_id=project_id, closet_id=closet_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        module_id = self.kwargs.get('module_pk')
        compartment_id = self.kwargs.get('compartment_pk')
        zone_id = self.kwargs.get('zone_pk')
        closet_id = self.kwargs.get('closet_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        if not module_id:
            raise ValidationError("Module ID is required")
        if not compartment_id:
            raise ValidationError("Compartment ID is required")
        if not zone_id:
            raise ValidationError("Zone ID is required")
        if not closet_id:
            raise ValidationError("Closet ID is required")
        serializer.save(project_id=project_id, closet_id=closet_id)


@path_params("project_pk", "module_pk", "compartment_pk", "zone_pk", "closet_pk", "inner_components_pk")
class ValueResourceInnerComponentViewSet(viewsets.ModelViewSet):
    serializer_class = ValueResourceInnerComponentSerializer

    def get_queryset(self):
        return ValueResourceInnerComponent.objects.filter(inner_component_id=self.kwargs["inner_component_pk"])

    def perform_create(self, serializer):
        serializer.save(inner_component_id=self.kwargs["inner_component_pk"])




# --------------------------  Missions ------------------------------------------

@path_params()
class MissionsViewSet(viewsets.ModelViewSet):
    serializer_class = MissionsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        return Mission.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        if not project_id:
            raise ValidationError("Project ID is required")
        serializer.save(project_id=project_id)


