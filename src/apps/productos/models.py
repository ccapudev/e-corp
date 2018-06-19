from django.db import models
from apps.syscore.models import AuditableModel


# Create your models here.
class Producto(AuditableModel):
    precio = models.DecimalField(
        "Precio de artículo", max_digits=8, decimal_places=2)
    moneda = models.ForeignKey("sistema.Moneda")
    nombre = models.CharField("Nombre de Artículo", max_length=50)
    prima = models.BooleanField("Es materia prima", default=True)
