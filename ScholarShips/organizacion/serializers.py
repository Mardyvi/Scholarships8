from dataclasses import fields
from urllib import response
from rest_framework import serializers
from .models import Organizacion 

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'

'''class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ["role"]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['role'] = OrgSerializer(instance.role).data
        return response
'''       

        