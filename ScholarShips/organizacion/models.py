from django.db import models

def upload_img(instance, filename):
    return f'imgs_org/{instance.nombre}/{filename}'

class Organizacion(models.Model):
    AREA_DE_INTERES_CHOICES = [
        ('Tecnología','Tecnología'),
        ('Salud','Salud'),
        ('Artes y Humanidades','Artes y Humanidades'),
        ('Ciencias Sociales','Ciencias Sociales'),
        ('Ingeniería','Ingeniería')
    ]
    
    nombre = models.CharField(max_length=56)
    pais = models.CharField(max_length=32)
    area = models.CharField(max_length=256, choices=AREA_DE_INTERES_CHOICES, default='Tecnología')
    email = models.EmailField(max_length=50, unique=True)
    web_page = models.URLField(max_length=256)
    tipo = models.BooleanField(default=True, verbose_name="Organización")
    image = models.ImageField(upload_to=upload_img, default='imgs_org/default.png',null=True)

    class Meta:
        db_table = 'orgs'
    
    def __str__(self) :
        return self.nombre

