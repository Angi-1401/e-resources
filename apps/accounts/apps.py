from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts"
    verbose_name = _("Cuentas de Usuario")

    def ready(self):
        from apps.accounts.signals import (
            create_main_groups_and_users,
            assign_user_to_group,
        )
