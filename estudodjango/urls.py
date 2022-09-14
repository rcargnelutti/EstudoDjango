from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from company.views import CompanyViewSet
from entity.views import EntityViewSet, UnityViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'entities', EntityViewSet)
router.register(r'units', UnityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Autenticação
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API
    path('api/', include(router.urls)),
]
