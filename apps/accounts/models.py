from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from uuid import uuid4


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, verbose_name=_("ID")
    )
    username = models.CharField(
        max_length=9,
        unique=True,
        validators=[
            RegexValidator(regex=r"^(V|E)[0-9]{7,8}$", message=_("Ejemplo: V12345678"))
        ],
        verbose_name=_("Cédula de Identidad"),
        help_text=_("Ejemplo: V12345678, E12345678"),
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")
