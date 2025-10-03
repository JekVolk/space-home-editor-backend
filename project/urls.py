from rest_framework_nested import routers

from .views import *

# 0 рівень (projects)
router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename="projects")

urlpatterns = []
urlpatterns += router.urls