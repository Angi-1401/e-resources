from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver

from apps.accounts.models import User


@receiver(post_migrate)
def create_main_groups_and_users(sender, **kwargs):
    admin_group, created = Group.objects.get_or_create(name="Administrador")
    moderador_group, created = Group.objects.get_or_create(name="Moderador")
    docente_group, created = Group.objects.get_or_create(name="Docente")
    lector_group, created = Group.objects.get_or_create(name="Lector")

    admin, created = User.objects.get_or_create(
        username="V00000000", is_staff=True, is_superuser=True
    )
    admin.set_password("V00000000")
    admin.groups.add(admin_group)
    admin.save()

    moderador, created = User.objects.get_or_create(username="V00000001")
    moderador.set_password("V00000001")
    moderador.groups.add(moderador_group)
    moderador.save()

    docente, created = User.objects.get_or_create(username="V00000002")
    docente.set_password("V00000002")
    docente.groups.add(docente_group)
    docente.save()

    lector, created = User.objects.get_or_create(username="V00000003")
    lector.set_password("V00000003")
    lector.groups.add(lector_group)
    lector.save()


@receiver(post_save, sender=User)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            group_name = "Administrador"
        else:
            group_name = "Lector"

        group, _ = Group.objects.get_or_create(name=group_name)
        instance.groups.add(group)
        instance.save()
