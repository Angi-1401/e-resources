from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UsernameField,
)
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (
                field.label if hasattr(field, "label") else "Error",
                error,
            )
    return msg


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "date_joined")

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "readonly": "readonly",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "readonly": "readonly",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "date_joined": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "readonly": "readonly",
                }
            ),
        }


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Contraseña"),
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Contraseña"}
        ),
    )
    password2 = forms.CharField(
        label=_("Confirmar Contraseña"),
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirmar contraseña"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )

        labels = {
            "username": _("Cédula de Identidad"),
            "email": _("Email"),
        }
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Cédula de identidad",
                    "help_text": "Ejemplo: V12345678, E12345678",
                }
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "example@provider.com"}
            ),
        }


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de usuario"}
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Contraseña"}
        ),
    )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
        label=_("Email"),
    )


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Nueva contraseña"}
        ),
        label=_("Nueva contraseña"),
    )
    new_password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirmar nueva contraseña"}
        ),
        label=_("Confirmar nueva contraseña"),
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Antigua contraseña"}
        ),
        label=_("Antigua contraseña"),
    )
    new_password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Nueva contraseña"}
        ),
        label=_("Nueva contraseña"),
    )
    new_password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirmar nueva contraseña"}
        ),
        label=_("Confirmar nueva contraseña"),
    )
