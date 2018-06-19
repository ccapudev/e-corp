from django.db import models
from uuid import uuid4
from apps.syscore.models import AuditableModel
from . import constantes as const


# Create your models here.
class Almacen(AuditableModel):
    nombre = models.CharField("Nombre de Almacén", max_length=50)
    direccion = models.CharField("Dirección", max_length=50)


class KardexConfig(AuditableModel):
    moneda_nativa = models.ForeignKey(
        "sistema.Moneda", verbose_name='Modeda Local')
    impuesto = models.DecimalField(
        "% de impuesto", max_digits=6, decimal_places=3)


class Kardex(AuditableModel):
    almacen = models.ForeignKey("almacen.Almacen")
    transaccion = models.CharField(
        "Tipo de transacción", max_length=50,
        choices=const.TIPOS_DE_TRANSACCION
    )
    cantidad_ingreso = models.DecimalField(
        "Cantidad Ingreso", max_digits=8, decimal_places=2)
    cantidad_salida = models.DecimalField(
        "Cantidad Salida", max_digits=8, decimal_places=2)
    precio_unitario = models.DecimalField(
        "Precio Unitario", max_digits=8, decimal_places=2)
    tipo_cambio = models.DecimalField(
        "Tipo Cambio", max_digits=5, decimal_places=3)
    moneda = models.ForeignKey("sistema.Moneda")

    monto_total = models.DecimalField(
        "Monto total", max_digits=10, decimal_places=2)
    monto_total_local = models.DecimalField(
        "Monto total (Moneda Local)", max_digits=12, decimal_places=2)
    monto_moneda = models.ForeignKey("sistema.Moneda", related_name='montos')

    impuesto = models.DecimalField("Impuesto (IGV, IVA)",
                                   max_digits=12, decimal_places=3)
