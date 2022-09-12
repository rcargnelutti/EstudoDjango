from django.urls import path, include
from rest_framework import routers
from company.views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'api', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
