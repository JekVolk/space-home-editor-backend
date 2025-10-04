from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.utils.html import format_html

from project.admin import CatalogInline, ProjectInline, ValueResourceCosmonautsInline, ValueResourceModuleInline, \
    ValueResourceExternalSystemInline, ValueResourceCompartmentInline, ValueResourceZoneInline, \
    ValueResourceClosetInline, ValueResourceComponentInline, ValueResourceInnerComponentInline
from project.models import ValueResourceCosmonauts
from .models import Catalog, Teg, Material, TegProject, Cosmonauts, Resource, DefaultResourceCosmonauts, \
    DefaultResourceCatalog, DefaultValueCatalog


# ==========================
# ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ДЛЯ МИНИАТЮР
# ==========================
def image_preview(obj):
    # Если у модели есть поле photo
    if hasattr(obj, "photo") and obj.photo:
        return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;"/>', obj.photo.url)
    # Если у модели есть поле icon
    if hasattr(obj, "icon") and obj.icon:
        return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;"/>', obj.icon.url)
    return "—"

image_preview.short_description = "Превью"


# ==========================
# CATALOG
# ==========================
@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'teg', 'user', image_preview)
    list_display_links = ('id', 'name')
    list_filter = ('type', 'teg', 'user')
    search_fields = ('name',)
    list_editable = ('type',)
    list_per_page = 20



# ==========================
# TEG
# ==========================
@admin.register(Teg)
class TegAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    search_fields = ('name',)
    list_filter = ('user',)
    inlines = [CatalogInline]

# ==========================
# MATERIAL
# ==========================
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', image_preview)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('user',)


# ==========================
# TEG PROJECT
# ==========================
@admin.register(TegProject)
class TegProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    search_fields = ('name',)
    list_filter = ('user',)
    inlines = [ProjectInline]


# ==========================
# COSMONAUTS
# ==========================
@admin.register(Cosmonauts)
class CosmonautsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', image_preview)
    search_fields = ('name',)
    list_filter = ('user',)


# ==========================
# RESOURCE
# ==========================
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'limit', 'is_limit_type_big', 'stock',
                    'is_stock_percentage', 'user', image_preview)
    list_filter = ('is_limit_type_big', 'is_stock_percentage', 'user')
    list_editable = ('limit', 'is_limit_type_big', 'stock', 'is_stock_percentage')
    search_fields = ('name',)
    inlines=[ValueResourceCosmonautsInline, ValueResourceModuleInline, ValueResourceExternalSystemInline,
             ValueResourceCompartmentInline, ValueResourceCompartmentInline, ValueResourceZoneInline, ValueResourceClosetInline,
             ValueResourceComponentInline,ValueResourceInnerComponentInline]




# ==========================
# DEFAULT RESOURCE
# ==========================
@admin.register(DefaultResourceCosmonauts)
class DefaultResourceCosmonautsAdmin(admin.ModelAdmin):
    list_display = ("id", "resource", "cosmonaut", "value", "is_disposable")
    list_filter = ("is_disposable", "resource", "cosmonaut")
    search_fields = ("cosmonaut__name", "resource__name")  # подстрой под реальные поля
    ordering = ("cosmonaut", "resource")


@admin.register(DefaultResourceCatalog)
class DefaultResourceCatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "resource", "value", "is_disposable")
    list_filter = ("is_disposable", "catalog", "resource")
    search_fields = ("catalog__name", "resource__name")
    ordering = ("catalog", "resource")


@admin.register(DefaultValueCatalog)
class DefaultValueCatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "w", "h", "d", "price", "weight", "comment")
    search_fields = ("catalog__name", "comment")
    ordering = ("catalog",)