from django.db import models
from django.utils import timezone
from django.templatetags.static import static

# Create your models here.

class Libros(models.Model):
    titulo = models.CharField(max_length = 50)
    autor  = models.CharField(max_length = 50)
    anio = models.IntegerField()
    reservado = models.BooleanField(default = False)
    libro_img = models.ImageField()

    @property
    def img_url(self):
        return static("media/{}".format(self.libro_img))

    def __str__(self):
        return "%s %s %i %i" % (self.titulo, self.autor, self.anio, self.reservado)

class Prestamos(models.Model):
    libro = models.ForeignKey(Libros, on_delete = models.CASCADE)
    usuario = models.CharField(max_length = 50)
    fecha = models.DateField(default = timezone.now)

    def __str__(self):
        return "%s" % (self.usuario)

class Usuarios(models.Model):
    usuario = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return "%s %s" % (self.usuario, self.password)
