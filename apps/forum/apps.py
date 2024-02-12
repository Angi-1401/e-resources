from django.apps import AppConfig


class ForumConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.forum"

    class Meta:
        verbose_name = "Foro"
        verbose_name_plural = "Foros"

    def ready(self):
        from apps.forum.signals import create_forum
