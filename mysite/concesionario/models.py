from django.db import models

# Create your models here.
class Inventario(models.Model):
    placa = models.CharField(null=False, max_length=6)
    modelo = models.CharField(null=True, max_length=20)
    descripcion = models.TextField(max_length=100)
    disponible = models.BooleanField(default=True)
    valor = models.IntegerField(null=False)

    def __str__(self):
        return self.placa