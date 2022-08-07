from django.db import models

# Create your models here.

class Organizacion(models.Model):
    ROLES = (
        ('Organizacion','Organizacion'),
        ('organizacion','organizacion'),
        ('Becado','Becado'),
        ('becado','becado')
    )

    nombre = models.CharField(max_length=56)
    pais = models.CharField(max_length=32)
    area = models.CharField(max_length=256)
    email = models.EmailField(max_length=50, unique=True)
    web_page = models.URLField(max_length=256)
    rol = models.CharField(max_length=50, choices=ROLES, null=True)
    
    class Meta:
        db_table = 'orgs'
    
    def __str__(self) :
        return self.nombre

