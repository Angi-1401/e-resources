from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from apps.accounts.forms import ProfileForm, form_validation_error
from apps.accounts.forms import (
    UserLoginForm,
    RegistrationForm,
    UserPasswordResetForm,
    UserSetPasswordForm,
    UserPasswordChangeForm,
)
from apps.accounts.models import User


@method_decorator(login_required(login_url="login"), name="dispatch")
class ProfileView(View):
    def get(self, request):
        profile_form = ProfileForm(instance=request.user)
        context = {"profile": profile_form, "segment": "profile"}
        return render(request, "accounts/profile.html", context)

    def post(self, request):
        profile_form = ProfileForm(request.POST, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile saved successfully")
        else:
            messages.error(request, "Error saving profile")

        return redirect("profile")


class UserLoginView(LoginView):
    template_name = "accounts/sign-in.html"
    form_class = UserLoginForm


def logout_view(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("¡Cuenta creada exitosamente!")
            return redirect("/accounts/login")
        else:
            print("¡Error al crear cuenta!")
    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, "accounts/sign-up.html", context)


class UserPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset.html"
    form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    form_class = UserSetPasswordForm


class UserPasswordChangeView(PasswordChangeView):
    template_name = "accounts/password_change.html"
    form_class = UserPasswordChangeForm
