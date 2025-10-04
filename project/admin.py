from django.contrib import admin

# Register your models here.



from django.contrib import admin

# Register your models here.


from django.utils.html import format_html

from user.models import Catalog
from .models import (
    Project, Mission,
    ExternalSystems, Module, Compartment, Zone, Component, Closet, InnerComponent,
    ValueResourceCosmonauts, ValueResourceModule, ValueResourceExternalSystem, ValueResourceCompartment,
    ValueResourceZone, ValueResourceComponent, ValueResourceInnerComponent, SettingsSpaceStation, ValueResourceCloset
)


class MissionInline(admin.TabularInline):  # можно использовать StackedInline
    model = Mission
    extra = 0

class CatalogInline(admin.TabularInline):
    model=Catalog
    extra=0

class ProjectInline(admin.TabularInline):
    model=Project
    extra=0


class ExternalSystemsInline(admin.TabularInline):
    model = ExternalSystems
    extra = 0

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0

class CompartmentInline(admin.TabularInline):
    model = Compartment
    extra = 0

class ZoneInline(admin.TabularInline):
    model = Zone
    extra = 0

class ComponentInline(admin.TabularInline):
    model = Component
    extra = 0

class ClosetInline(admin.TabularInline):
    model = Closet
    extra = 0

class InnerComponentInline(admin.TabularInline):
    model = InnerComponent
    extra = 0

class ValueResourceModuleInline(admin.TabularInline):
    model = ValueResourceModule
    extra = 0


class  ValueResourceExternalSystemInline(admin.TabularInline):
    model = ValueResourceExternalSystem
    extra = 0

class ValueResourceCompartmentInline(admin.TabularInline):
    model = ValueResourceCompartment
    extra = 0

class ValueResourceZoneInline(admin.TabularInline):
    model = ValueResourceZone
    extra = 0

class ValueResourceClosetInline(admin.TabularInline):
    model = ValueResourceCloset
    extra = 0

class ValueResourceComponentInline(admin.TabularInline):
    model = ValueResourceComponent
    extra = 0

class ValueResourceInnerComponentInline(admin.TabularInline):
    model = ValueResourceInnerComponent
    extra = 0

class ValueResourceCosmonautsInline(admin.TabularInline):
    model = ValueResourceCosmonauts
    extra = 0



# =====================
# Вспомогательная функция для превью картинок
# =====================
def preview_image(obj):
    if hasattr(obj, "preview") and obj.preview:
        return format_html('<img src="{}" width="60" height="40" style="object-fit:cover;border-radius:4px;"/>', obj.preview.url)
    return "—"
preview_image.short_description = "Превью"


# =====================
# PROJECT
# =====================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "teg", preview_image, "created_at", "updated_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "description", "user__username", "teg__name")
    list_filter = ("user", "teg")
    list_per_page = 20
    inlines = [MissionInline, ExternalSystemsInline, ModuleInline]




# =====================
# MISSION
# =====================
@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "project", "days", "crew_number")
    list_filter = ("project",)
    search_fields = ("name", "description")
    filter_horizontal = ("cosmonauts",)


# =====================
# SETTINGS
# =====================
@admin.register(SettingsSpaceStation)
class SettingsSpaceStationAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "recursive_water", "max_weight")
    list_filter = ("project",)


# =====================
# BASE CLASSES (ExternalSystems, Module, Compartment, Zone, Component, Closet, InnerComponent)
# =====================
@admin.register(ExternalSystems)
class ExternalSystemsAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "project")
    list_filter = ("project", "catalog")
    inlines=[ValueResourceExternalSystemInline]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "project", "material", "owner")
    list_filter = ("project", "catalog", "material")
    search_fields = ("owner",)
    inlines = [CompartmentInline, ValueResourceModuleInline]


@admin.register(Compartment)
class CompartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "project", "module")
    list_filter = ("project", "catalog", "module")
    inlines = [ZoneInline, ValueResourceCompartmentInline]



@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "project", "compartment")
    list_filter = ("project", "catalog", "compartment")
    inlines = [ComponentInline, ClosetInline, ValueResourceZoneInline]




@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "project", "zone")
    list_filter = ("project", "catalog", "zone")
    inlines=[ValueResourceComponentInline]


@admin.register(Closet)
class ClosetAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "project", "zone")
    list_filter = ("project", "catalog", "zone")
    inlines = [InnerComponentInline, ValueResourceClosetInline]


@admin.register(InnerComponent)
class InnerComponentAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "project", "closets")
    list_filter = ("project", "catalog", "closets")
    inlines = [ValueResourceInnerComponentInline]


# =====================
# VALUE RESOURCE
# =====================

@admin.register(ValueResourceCosmonauts)
class ValueResourceCosmonautsAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "resource", "cosmonaut")
    list_filter = ("project", "resource", "cosmonaut")
    search_fields = ("project__name", "resource__name", "cosmonaut__name")
    ordering = ("project", "resource", "cosmonaut")


@admin.register(ValueResourceModule)
class ValueResourceModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "resource", "module")
    list_filter = ("project", "resource", "module")
    search_fields = ("project__name", "resource__name", "module__name")
    ordering = ("project", "resource", "module")


@admin.register(ValueResourceExternalSystem)
class ValueResourceExternalSystemAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "resource", "external_system")
    list_filter = ("project", "resource", "external_system")
    search_fields = ("project__name", "resource__name", "external_system__name")
    ordering = ("project", "resource", "external_system")





@admin.register(ValueResourceCompartment)
class ValueResourceCompartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "resource", "compartment")
    list_filter = ("project", "resource", "compartment")
    search_fields = ("project__name", "resource__name", "compartment__name")
    ordering = ("project", "resource", "compartment")


@admin.register(ValueResourceZone)
class ValueResourceZoneAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "resource", "zone")
    list_filter = ("project", "resource", "zone")
    search_fields = ("project__name", "resource__name", "zone__name")
    ordering = ("project", "resource", "zone")



@admin.register(ValueResourceComponent)
class ValueResourceComponentAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "resource", "cosmonaut")
    list_filter = ("project", "resource", "cosmonaut")
    search_fields = ("project__name", "resource__name", "cosmonaut__name")
    ordering = ("project", "resource", "cosmonaut")


@admin.register(ValueResourceInnerComponent)
class ValueResourceInnerComponentAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "resource", "inner_component")
    list_filter = ("project", "resource", "inner_component")
    search_fields = ("project__name", "resource__name", "inner_component__name")
    ordering = ("project", "resource", "inner_component")