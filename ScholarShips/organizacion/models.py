from django.db import models

def upload_img(instance, filename):
    return f'imgs_org/{instance.nombre}/{filename}'

class Organizacion(models.Model):
    
    nombre = models.CharField(max_length=56)
    pais = models.CharField(max_length=32)
    area = models.CharField(max_length=256)
    email = models.EmailField(max_length=50, unique=True)
    web_page = models.URLField(max_length=256)
    tipo = models.BooleanField(default=False, verbose_name="Organización")
    image = models.ImageField(upload_to=upload_img, default='imgs_org/default.png',null=True)

    class Meta:
        db_table = 'orgs'
    
    def __str__(self) :
        return self.nombre

