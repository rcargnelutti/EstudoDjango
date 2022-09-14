from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers
from company.models import Company
from django.contrib.auth.models import User

class CompanySerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = CharField(source="user.id")
    user_username = CharField(source="user.username")
    user_mail = CharField(source="user.email")
    
    class Meta:
        model = Company
        fields = '__all__'