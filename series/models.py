from django.db import models
from django.conf import settings
from django.utils import timezone

class Publicacion(models.Model):
    nombre = models.CharField(max_length=200)
    episodios = models.PositiveIntegerField(default=1)
    temporadas = models.PositiveIntegerField(default=1)
    imagen = models.URLField(blank=True, null=True)
    año = models.DateField(blank=True, null=True)
    pais= models.CharField(max_length=200,blank=True, null=True)  

    rating_resumen=models.URLField(
    verbose_name="Ver breve resumen"
    )

    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

def __str__(self):
    return self.nombre