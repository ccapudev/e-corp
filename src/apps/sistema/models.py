from django.db import models


# Create your models here.
class Moneda(models.Model):
    nombre = models.CharField("Nombre de Moneda", max_length=50)
    codigo = models.CharField("Código de Moneda", max_length=50)
    tipo_cambio = models.DecimalField(
        "Tipo de Cambio", max_digits=6, decimal_places=3)
