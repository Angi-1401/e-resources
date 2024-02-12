import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from apps.accounts.models import User
from apps.library.models import Resource


class Forum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, verbose_name=_("Recurso")
    )
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Fecha de Creación")
    )

    class Meta:
        verbose_name = _("Foro")
        verbose_name_plural = _("Foros")

    def __str__(self):
        return self.resource.title

    @property
    def get_posts(self):
        return Post.objects.filter(forum=self)

    @property
    def last_post(self):
        return Post.objects.filter(forum=self).latest("timestamp")


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name=_("Foro"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Usuario"))
    title = models.CharField(max_length=255, verbose_name=_("Título"))
    content = HTMLField(verbose_name=_("Contenido"))
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Fecha de Creación")
    )

    class Meta:
        verbose_name = _("Publicación")
        verbose_name_plural = _("Publicaciones")

    def __str__(self):
        return self.timestamp

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])


class Reply(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name=_("Publicación")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Usuario"))
    content = HTMLField(verbose_name=_("Contenido"))
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Fecha de Creación")
    )

    class Meta:
        verbose_name = _("Respuesta")
        verbose_name_plural = _("Respuestas")

    def __str__(self):
        return self.timestamp


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reply = models.ForeignKey(
        Reply, on_delete=models.CASCADE, verbose_name=_("Respuesta")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Usuario"))
    content = HTMLField(verbose_name=_("Contenido"))
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Fecha de Creación")
    )

    class Meta:
        verbose_name = _("Comentario")
        verbose_name_plural = _("Comentarios")

    def __str__(self):
        return self.timestamp
