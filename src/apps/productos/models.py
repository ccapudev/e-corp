from django.db import models
from apps.syscore.models import AuditableModel


class Categoria(AuditableModel):
	nombre = models.CharField("Nombre", max_length=50)
	relacion = models.ForeignKey(
		"self", verbose_name='Categoría padre', null=True, blank=True)

class Producto(AuditableModel):
	categoria = models.ForeignKey("producto.Categoria")
    precio = models.DecimalField(
        "Precio de artículo", max_digits=8, decimal_places=2)
    moneda = models.ForeignKey("sistema.Moneda")
    nombre = models.CharField("Nombre de Artículo", max_length=50)
    prima = models.BooleanField("Es materia prima", default=True)
