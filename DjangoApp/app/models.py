from django.db import models
from django.utils import timezone

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length = 30)
    autor  = models.CharField(max_length = 30)
    anio = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.titulo, self.autor)

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete = models.CASCADE)
    fecha = models.DateField(default = timezone.now)
    usuario = models.CharField(max_length = 50)

    def __str__(self):
        return "%s" % (self.usuario)
