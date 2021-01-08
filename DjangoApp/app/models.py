from django.db import models
from django.utils import timezone

# Create your models here.

class Libros(models.Model):
    titulo = models.CharField(max_length = 50)
    autor  = models.CharField(max_length = 50)
    anio = models.IntegerField()
    reservado = models.BooleanField(default = False)

    def __str__(self):
        return "%s %s %i %i" % (self.titulo, self.autor, self.anio, self.reservado)

class Prestamos(models.Model):
    libro = models.ForeignKey(Libros, on_delete = models.CASCADE)
    fecha = models.DateField(default = timezone.now)

    def __str__(self):
        return "%s" % (self.usuario)
