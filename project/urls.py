from rest_framework_nested import routers
from .views import *

# 0 рівень (projects)
router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename="projects")

# 1 рівень (project → modules, external_systems)
projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'modules', ModuleViewSet, basename='project-modules')
projects_router.register(r'external-systems', ExternalSystemsViewSet, basename='project-external-systems')

# 2.1 рівень (module → compartments, value-resource)
modules_router = routers.NestedSimpleRouter(projects_router, r'modules', lookup='module')
modules_router.register(r'compartments', CompartmentViewSet, basename='module-compartments')
modules_router.register(
    r'value-resource',
    ValueResourceModuleViewSet,
    basename='module-value-resource'
)

# 2.2 рівень (external_systems → value-resource)
external_systems_router = routers.NestedSimpleRouter(projects_router, r'external-systems', lookup='external_system')
external_systems_router.register(
    r'value-resource',
    ValueResourceExternalSystemViewSet,
    basename='external-systems-value-resource'
)

# 3 рівень (compartment → zones, value-resource)
compartments_router = routers.NestedSimpleRouter(modules_router, r'compartments', lookup='compartment')
compartments_router.register(r'zones', ZoneViewSet, basename='compartment-zones')
compartments_router.register(
    r'value-resource',
    ValueResourceCompartmentViewSet,
    basename='compartment-value-resource'
)

# 4 рівень (zone → components, closets, value-resource)
zones_router = routers.NestedSimpleRouter(compartments_router, r'zones', lookup='zone')
zones_router.register(r'components', ComponentViewSet, basename='zone-components')
zones_router.register(r'closets', ClosetViewSet, basename='zone-closets')
zones_router.register(
    r'value-resource',
    ValueResourceZoneViewSet,
    basename='zone-value-resource'
)

# 5.1 рівень (closet → inner_components, value-resource)
closets_router = routers.NestedSimpleRouter(zones_router, r'closets', lookup='closet')
closets_router.register(r'inner-components', InnerComponentViewSet, basename='closet-inner-components')
closets_router.register(
    r'value-resource',
    ValueResourceClosetViewSet,
    basename='closet-value-resource'
)

# 5.2 рівень (components → value-resource)
components_router = routers.NestedSimpleRouter(zones_router, r'components', lookup='components')
components_router.register(
    r'value-resource',
    ValueResourceComponentViewSet,
    basename='components-value-resource'
)

# 6 рівень (inner_components → value-resource)
inner_components = routers.NestedSimpleRouter(closets_router, r'inner-components', lookup='inner_components')
inner_components.register(
    r'value-resource',
    ValueResourceInnerComponentViewSet,
    basename='inner-components-value-resource'
)

urlpatterns = []
urlpatterns += router.urls
urlpatterns += projects_router.urls
urlpatterns += modules_router.urls
urlpatterns += external_systems_router.urls
urlpatterns += compartments_router.urls
urlpatterns += zones_router.urls
urlpatterns += closets_router.urls
urlpatterns += components_router.urls
urlpatterns += inner_components.urls