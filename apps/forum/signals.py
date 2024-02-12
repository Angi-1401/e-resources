from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.forum.models import Forum
from apps.library.models import Resource


@receiver(post_save, sender=Resource)
def create_forum(sender, instance, created, **kwargs):
    if created:
        Forum.objects.get_or_create(resource=instance)
