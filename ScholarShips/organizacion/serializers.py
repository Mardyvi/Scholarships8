from dataclasses import fields
from urllib import response
from rest_framework import serializers
from .models import Organizacion 

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'

class OrgListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = (
            'id',
            'nombre',
            'image'
            )

