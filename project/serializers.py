from rest_framework import serializers

from project.models import Project, SettingsSpaceStation, Module, ExternalSystems, ValueResourceModule, \
    ValueResourceExternalSystem, Compartment, ValueResourceCompartment, Zone, ValueResourceZone, Component, \
    ValueResourceComponent, Closet, ValueResourceCloset, InnerComponent, ValueResourceInnerComponent, Mission



# -------------------------- Project ------------------------------------------

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "description", "teg", "preview", "created_at", "updated_at")
        read_only_fields = ['id', "created_at", "updated_at"]

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsSpaceStation
        fields = ["recursive_water", "max_weight", "max_price"]

# -------------------------- Module ------------------------------------------

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ("id", "name", "comment", "weight", "price", "x", "y", "z", "w", "h", "orient", "material", "owner", "catalog")
        read_only_fields = ('id',)

class ValueResourceModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueResourceModule
        fields = ("id", "value", "is_disposable", "resource")
        read_only_fields = ('id',)

# -------------------------- ExternalSystems ------------------------------------------

class ExternalSystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalSystems
        fields = ("id", "name", "comment", "weight", "price", "x", "y", "z", "w", "h", "d", "orient", "catalog")
        read_only_fields = ('id')

class ValueResourceExternalSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueResourceExternalSystem
        fields = ("id", "value", "is_disposable", "resource")
        read_only_fields = ('id',)

# -------------------------- Compartment ------------------------------------------

class CompartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compartment
        fields = ("id", "name", "comment", "weight", "price", "x", "y", "z", "w", "h", "d", "catalog")
        read_only_fields = ('id')

class ValueResourceCompartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueResourceCompartment
        fields = ("id", "value", "is_disposable", "resource")
        read_only_fields = ('id',)

# -------------------------- Zone ------------------------------------------

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ("id", "name", "comment", "weight", "price", "x", "y", "z", "w", "h", "d", "catalog")

class ValueResourceZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueResourceZone
        fields = ("id", "value", "is_disposable", "resource")
        read_only_fields = ('id',)

# -------------------------- Component ------------------------------------------

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ("id", "name", "comment", "weight", "price", "x", "y", "z", "w", "h", "d", "orient", "catalog")

class ValueResourceComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueResourceComponent
        fields = ("id", "value", "is_disposable", "resource")
        read_only_fields = ('id',)

# -------------------------- Closet ------------------------------------------

class ClosetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Closet
        fields = ("id", "name", "comment", "weight", "price", "x", "y", "z", "w", "h", "d", "catalog")

class ValueResourceClosetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueResourceCloset
        fields = ("id", "value", "is_disposable", "resource")
        read_only_fields = ('id',)

# -------------------------- InnerComponent ------------------------------------------

class InnerComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InnerComponent
        fields = ("id", "name", "comment", "weight", "price", "x", "y", "z", "w", "h", "d", "orient", "catalog")

class ValueResourceInnerComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueResourceInnerComponent
        fields = ("id", "value", "is_disposable", "resource")
        read_only_fields = ('id',)



# -------------------------- Mission ------------------------------------------

class MissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ("name", "days", "description", "crew_number")
        read_only_fields = ('id',)


