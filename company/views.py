from xmlrpc.client import boolean
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from company.models import Company
from company.serializers import CompanySerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'document','active']
    # http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']

    # sobrescrevendo queryset para filtrar/buscar por companies active
    # def get_queryset(self):
    #     company = Company.objects.filter(active=True, name='AVACON')
    #     return company

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     active = self.request.query_params.get('active')
    #     qs = qs.filter(active=active)
    #     return qs

    # def get_queryset(self):
    #     qs = Company.objects.all()
    #     active = self.request.query_params.get('active')
    #     print(active)
    #     # if active is not None:
    #     qs = qs.filter(active=active)
    #     return qs

