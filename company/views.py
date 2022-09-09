from rest_framework.viewsets import ModelViewSet

from company.models import Company
from company.serializers import CompanySerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
