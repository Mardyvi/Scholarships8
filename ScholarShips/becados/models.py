from django.db import models
from django.utils.translation import gettext_lazy as _


class Becado(models.Model):
    NOMBRE = models.CharField(max_length=50)
    APELLIDO_PATERNO = models.CharField(max_length=50)
    APELLIDO_MATERNO = models.CharField(max_length=50)
    CORREO_ELECTRONICO = models.EmailField(max_length=254)
    AREA_DE_INTERES_CHOICES = [
        ('Tecnología', 'Tecnología'),
        ('Salud', 'Salud'),
        ('Artes y Humanidades', 'Artes y Humanidades'),
        ('Ciencias_Sociales', 'Ciencias Sociales'),
        ('Ingenería', 'Ingenería')
    ]
    area_de_interes  = models.CharField(
        max_length=20,
        choices = AREA_DE_INTERES_CHOICES,
        default = 'Tecnología',
    )
    GRADO_ACADEMICO_CHOICES = [
        ('Licenciatura', 'Licenciatura'),
        ('Maestria', 'Maestria'),
        ('Doctorado', 'Doctorado'),
        ('Curso', 'Curso')
    ]
    grado_academico = models.CharField(
        max_length=15,
        choices = GRADO_ACADEMICO_CHOICES,
        default = 'Curso',
    )
    
    ESTATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Egresado', 'Egresado')
    ]
    Estatus = models.CharField(
        max_length=15,
        choices = ESTATUS_CHOICES,
        default = 'Activo'
    )
    
    