from django.db import models
from django.utils.translation import gettext_lazy as _
#from django.db .becas import id_beca
#from django.db .comunidad import id_comunidad
#from django.db .rol import id_rol

class Becado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=254)
    class area_de_interes(models.TextChoices):
        Tecnología = _('Tecnología')
        Salud = _('Salud')
        Artes_y_Humanidades = _('Artes y Humanidades')
        Ciencias_Sociales = _('Ciencias Sociales')
        Ingenería = _('Ingenería')
    area_de_interes = models.CharField(
        max_length=20,
        choices = area_de_interes.choices,
        default = area_de_interes.Tecnología
    )
    class grado_academico(models.TextChoices):
        Licenciatura = _('Licenciatura')
        Maestria = _('Maestria')
        Doctorado = _('Doctorado')
        Curso = _('Curso')
    grado_academico = models.CharField(
        max_length=15,
        choices = grado_academico.choices,
        default = grado_academico.Curso
    )
    
    class Estatus(models.TextChoices):
        Activo = _('Activo')
        Egresado = _('Egresado')
    
    #id_beca = models.ForeignKey(Becas.Becas)
    #id_comunidad = models.ForeignKey(Comunidad.comunidad)
    #id_rol = models.OneToOneField(rol.rol)