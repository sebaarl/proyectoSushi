from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=80, null=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    tipo = models.ForeignKey(Tipo, on_delete=CASCADE)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True)
    descripcion = models.TextField()
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre