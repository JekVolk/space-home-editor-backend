from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers



from .views import RegisterView, LogoutView, CatalogViewSet, DefaultResourceCatalogViewSet, ResourcesViewSet, \
    MaterialsViewSet

router = DefaultRouter()
router.register(r'catalogs', CatalogViewSet, basename="catalog")
router.register(r'resources', ResourcesViewSet, basename="resource")
router.register(r'materials', MaterialsViewSet, basename="material")

# 1 рівень (catalogs → modules, default-resources)
default_resources_router = routers.NestedSimpleRouter(router, r'catalogs', lookup='catalog')
default_resources_router.register(r'default-resources', DefaultResourceCatalogViewSet, basename='catalog-default-resources')

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
urlpatterns += router.urls
urlpatterns += default_resources_router.urls