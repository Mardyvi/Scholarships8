from rest_framework import serializers
from .models import Beca


class BecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beca
        fields = [
            'id',
            #'organizacion',
            'nombrebeca',
            'descripcion',
        ]
"""
    def to_representation(self, instance):
        
        return {
            'id': instance.id,
            'organizacion': {
                'id': instance.organizacion.id,
                'name': instance.organizacion.name
                },
            'nombrebeca': instance.nombrebeca,
            'descripcion': instance.descripcion
        }
"""

