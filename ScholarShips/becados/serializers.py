from random import choices
from unittest.util import _MAX_LENGTH
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from becados.models import Becado

class BecadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Becado
        fields = '__all__'