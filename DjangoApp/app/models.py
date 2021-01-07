from django.db import models
from django.utils import timezone

# Create your models here.

class Libros(models.Model):
    titulo = models.CharField(max_length = 50)
    autor  = models.CharField(max_length = 50)
    anio = models.IntegerField()

    def __str__(self):
        return "%s %s %i" % (self.titulo, self.autor,self.anio)

class prestamos(models.Model):
    libro = models.ForeignKey(Libros, on_delete = models.CASCADE)
    fecha = models.DateField(default = timezone.now)
    usuario = models.CharField(max_length = 50)

    def __str__(self):
        return "%s" % (self.usuario)

class usuarios(models.Model):
    usuario = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return "%s %s" % (self.usuario, self.password)
