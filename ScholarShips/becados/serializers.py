from unittest.util import _MAX_LENGTH
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from becados.models import Becado

class BecadoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=50)
    apellido_paterno = serializers.CharField(required=True, allow_blank=False, max_length=50)
    apellido_materno = serializers.CharField(required=True, allow_blank=False, max_length=50)
    correo_electronico = serializers.EmailField(required=True, allow_blank=False, max_length=254)
    class area_de_interes(serializers.MultipleChoiceField):
        Tecnología = _('Tecnología')
        Salud = _('Salud')
        Artes_y_Humanidades = _('Artes y Humanidades')
        Ciencias_Sociales = _('Ciencias Sociales')
        Ingenería = _('Ingenería')
    area_de_interes = serializers.MultipleChoiceField(
        max_length=20,
        choices = area_de_interes.choices,
        default = area_de_interes.Tecnología
    )
    class grado_academico(serializers.MultipleChoiceField):
        Licenciatura = _('Licenciatura')
        Maestria = _('Maestria')
        Doctorado = _('Doctorado')
        Curso = _('Curso')
    grado_academico = serializers.MultipleChoiceField(
        max_length=15,
        choices = grado_academico.choices,
        default = grado_academico.Curso
    )
    
    class Estatus(serializers.MultipleChoiceField):
        Activo = _('Activo')
        Egresado = _('Egresado')
    Estatus = serializers.MultipleChoiceField(
        max_length=15,
        choices = Estatus.choices,
        default = Estatus.Activo
    )
    
    #id_beca = models.ForeignKey(Becas.Becas)
    #id_comunidad = models.ForeignKey(Comunidad.comunidad)
    #id_rol = models.OneToOneField(rol.rol)