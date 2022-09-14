from rest_framework.serializers import ModelSerializer, CharField
from entity.models import Entity, Unity, Company


class EntitySerializer(ModelSerializer):
    #company = CharField(source="company.name")
    class Meta:
        model = Entity
        fields = '__all__'
        #depth = 1    


class UnitySerializer(ModelSerializer):
    class Meta:
        model = Unity
        fields = '__all__'
        # depth = 2