from .models import Comunidad
from dataclasses import field, fields
from rest_framework import serializers

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields = '__all__'
