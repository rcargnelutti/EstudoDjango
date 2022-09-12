from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from company.views import CompanyViewSet
from entity.views import EntityViewSet, UnityViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'entities', EntityViewSet)
router.register(r'units', UnityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
