from django.urls import path, include
from rest_framework import routers
from entity.views import EntityViewSet

router = routers.DefaultRouter()
router.register(r'api', EntityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
