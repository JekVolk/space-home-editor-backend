from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import RegisterView, LogoutView, CatalogViewSet

router = DefaultRouter()
router.register(r'catalogs', CatalogViewSet, basename="catalog")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
urlpatterns += router.urls