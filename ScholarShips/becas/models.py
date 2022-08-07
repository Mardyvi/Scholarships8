from django.db import models
#from organizaciones.models import Organizacion

# Create your models here.

class Beca(models.Model):

    #organizacion = models.ForeignKey (Organizacion, on_delete=models.CASCADE)
    nombrebeca = models.CharField (max_length=50)
    descripcion = models.CharField (max_length=500)

    class Meta:
        db_table = 'becas'

    def __str__(self):
        return self.becas
