from rest_framework.viewsets import ModelViewSet
from entity.models import Entity, Unity
from entity.serializers import EntitySerializer, UnitySerializer

class EntityViewSet(ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class UnityViewSet(ModelViewSet):
    queryset = Unity.objects.all()
    serializer_class = UnitySerializer