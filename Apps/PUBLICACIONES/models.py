
# Create your models here.

from django.db import models

class Publicacion(models.Model):
	titulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=100)
	fecha = models.DateField()
	categoria = models.CharField(max_length=50)
	contenido = models.TextField()
	estado = models.CharField(max_length=20)
	imagen = models.URLField(blank=True)
	etiquetas = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.titulo
