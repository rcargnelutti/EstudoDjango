from rest_framework.viewsets import ModelViewSet
from entity.models import Entity
from entity.serializers import EntitySerializer

class EntityViewSet(ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer