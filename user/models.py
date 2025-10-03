from django.contrib.auth.models import User
from django.db import models


class Catalog(models.Model):
    class TypeCatalog(models.TextChoices):
        EXTERNAL_SYSTEMS = "ES", "external-systems"
        COMPONENTS = "CO", "components"
        CLOSETS = "SL", "closets"
        ZONES = "ZN", "zones"
        COMPARTMENTS = "CM", "compartments"
        MODULES = "MO", "modules"

    type = models.CharField(
        max_length=2,
        choices=TypeCatalog.choices,
    )

    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="catalog_photo/")  # catalog_photo
    teg = models.ForeignKey('Teg', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, related_name="catalogs", on_delete=models.CASCADE, blank=True, null=True)


class Teg(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="tegs", on_delete=models.CASCADE)


class Material(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="material_photo/")
    user = models.ForeignKey(User, related_name="materials", on_delete=models.CASCADE)


class TegProject(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="teg_projects", on_delete=models.CASCADE)


class Cosmonauts(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="cosmonauts_avatar/")
    user = models.ForeignKey(User, related_name="cosmonauts", on_delete=models.CASCADE)


class Resource(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="res_icons/", blank=True, null=True)
    limit = models.IntegerField()
    is_limit_type_big = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    is_stock_percentage = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="resources", on_delete=models.CASCADE, blank=True, null=True)


class DefaultResourceCosmonauts(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="default_resources_catalogs")
    value = models.IntegerField()
    is_disposable = models.BooleanField(default=False)
    cosmonaut = models.ForeignKey(Cosmonauts, on_delete=models.CASCADE,related_name="default_resources")

class DefaultResourceCatalog(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="default_resources_cosmonauts")
    value = models.IntegerField()
    is_disposable = models.BooleanField(default=False)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="default_resources")

class DefaultValueCatalog(models.Model):
    catalog=models.OneToOneField(Catalog, on_delete=models.CASCADE, related_name="default_value")
    w = models.PositiveIntegerField(null=True, blank=True)
    h = models.PositiveIntegerField(null=True, blank=True)
    d = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(blank=True, null=True)