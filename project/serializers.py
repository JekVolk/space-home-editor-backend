from rest_framework import serializers

from project.models import Project, SettingsSpaceStation

# -------------------------- Project ------------------------------------------

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "description", "preview", "created_at", "updated_at")
        read_only_fields = ['id', "created_at", "updated_at"]

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsSpaceStation
        fields = ["recursive_water", "max_weight"]