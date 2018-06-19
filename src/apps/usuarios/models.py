from django.db import models
from django.contrib.auth.models import User, Permission, Group
from uuid import uuid4
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver

# Create your models here.


class PerfilUsuario(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        primary_key=True, related_name='perfil')
    fecha_nacimiento = models.DateField(
        'Fecha Nacimiento', null=True, blank=True
    )
    uid = models.UUIDField("UUID de Perfil", default=uuid4, null=True)

    def __str__(self):
        return 'Perfil de %s' % self.user.username


@receiver(post_save, sender='auth.User')
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)
