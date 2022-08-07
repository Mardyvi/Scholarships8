from django.db import models

# Create your models here.

class Comunidad(models.Model):
    AreaInteres = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedIn = models.CharField(max_length=50)
    #beca = models.ForeignKey(Beca, on_delete=models.CASCADE)

    class Meta:
        db_table ='Comunidad' #nombre de la tabla en la base de datos

    def __str__(self):
        return self.AreaInteres

