from rest_framework.serializers import ModelSerializer
from entity.models import Entity, Unity

class EntitySerializer(ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'


class UnitySerializer(ModelSerializer):
    class Meta:
        model = Unity
        fields = '__all__'
