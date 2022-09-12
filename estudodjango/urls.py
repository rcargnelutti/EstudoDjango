from django.contrib import admin
from django.urls import path, include

# from rest_framework import routers

# from company.views import CompanyViewSet
# from entity.views import EntityViewSet

# router = routers.DefaultRouter()
# router.register(r'companies', CompanyViewSet)
# router.register(r'entities', EntityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),

    path('api/company/', include('company.urls')),
    path('api/entity/', include('entity.urls')),
    
]
