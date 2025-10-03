from django.contrib.auth.models import User
from django.db import models

from project.mixins import TimestampMixin, BasePropertyMixin, Size3DMixin, CordMixin, ValueResourceMixin, OrientedMixin, \
    Size2DMixin
from user.models import TegProject, Cosmonauts, Catalog, Resource, Material


class Project(TimestampMixin, models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    teg=models.ForeignKey(TegProject, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True, null=True)
    preview= models.ImageField(upload_to="project_preview/")


class Mission(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE,blank=True, null=True, related_name="missions")
    name=models.CharField(max_length=100)
    days=models.PositiveIntegerField()
    crew_number=models.PositiveIntegerField()
    description=models.TextField(blank=True, null=True)
    cosmonauts = models.ManyToManyField(Cosmonauts, related_name="missions")


class SettingsSpaceStation(models.Model):
    project=models.OneToOneField(Project, on_delete=models.CASCADE, related_name="settings")
    recursive_water=models.PositiveIntegerField(default=95)
    max_weight=models.PositiveIntegerField(blank=True, null=True)


class ExternalSystems(BasePropertyMixin, Size3DMixin, CordMixin, OrientedMixin, models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="external_systems")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="external_systems")


class Module(BasePropertyMixin, Size2DMixin, CordMixin, OrientedMixin, models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="modules")
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="modules")
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, blank=True, null=True, related_name="modules")
    owner = models.CharField(max_length=100,blank=True, null=True)

class Compartment(BasePropertyMixin, Size3DMixin, CordMixin, models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="compartments")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="compartments" )
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="compartments" )

class Zone(BasePropertyMixin, Size3DMixin, CordMixin, models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="zones")
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="zones")
    compartment = models.ForeignKey(Compartment, on_delete=models.CASCADE,related_name="zones")

class Component(BasePropertyMixin, Size3DMixin, CordMixin, OrientedMixin, models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="components")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="components")
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="components")


class Closet(BasePropertyMixin, Size3DMixin, CordMixin, models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="closets")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="closets")
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="closets")

class InnerComponent(BasePropertyMixin, Size3DMixin, CordMixin, OrientedMixin, models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="inner_components")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="inner_components")
    closets=models.ForeignKey(Closet, on_delete=models.CASCADE, related_name="inner_components")

class ValueResourceCosmonauts(ValueResourceMixin, models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="value_resources_cosmonauts")
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="values_resources_cosmonauts")
    cosmonaut=models.ForeignKey(Cosmonauts, on_delete=models.CASCADE, related_name="value_resources")

class ValueResourceModule(ValueResourceMixin, models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="value_resources_modules")
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="values_resources_modules")
    module=models.ForeignKey(Module, on_delete=models.CASCADE, related_name="value_resources")

class ValueResourceExternalSystem(ValueResourceMixin, models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="value_resources_external_systems")
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="values_resources_external_systems")
    external_system=models.ForeignKey(ExternalSystems, on_delete=models.CASCADE, related_name="value_resources")

class ValueResourceCompartment(ValueResourceMixin, models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="value_resources_compartments")
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="values_resources_compartments")
    compartment=models.ForeignKey(Compartment, on_delete=models.CASCADE, related_name="value_resources")

class ValueResourceZone(ValueResourceMixin, models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="value_resources_zones")
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="values_resources_zones")
    zone=models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="value_resources")

class ValueResourceCloset(ValueResourceMixin, models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="value_resources_closets")
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="values_resources_closets")
    closet=models.ForeignKey(Closet, on_delete=models.CASCADE, related_name="value_resources")

class ValueResourceComponent(ValueResourceMixin, models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="value_resources_components")
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="values_resources_components")
    cosmonaut=models.ForeignKey(Component, on_delete=models.CASCADE, related_name="value_resources")

class ValueResourceInnerComponent(ValueResourceMixin, models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="value_resources_inner_components")
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="values_resources_inner_components")
    inner_component=models.ForeignKey(InnerComponent, on_delete=models.CASCADE, related_name="value_resources")

