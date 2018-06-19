from django.db import models
from uuid import uuid4


# Create your models here.
class AuditableModel(models.Model):
    uid = models.UUIDField("UID", default=uuid4)
    fecha_creacion = models.DateTimeField("Fecha Creación", auto_now_add=True)
    fecha_modificacion = models.DateTimeField(
        "Fecha Modificación", auto_now=True)
