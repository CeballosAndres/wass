from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from .models import Asesorado, Asesor


def post_save_user(sender, instance, created, **kwargs):
    if created:
        if instance.username.isdigit():
            group = Group.objects.get(name='asesorados')
            instance.groups.add(group)
            Asesorado.objects.create(
                usuario=instance,
            )
        else:
            group = Group.objects.get(name='asesores')
            instance.groups.add(group)
            Asesor.objects.create(
                usuario=instance,
            )


post_save.connect(post_save_user, sender=User)
