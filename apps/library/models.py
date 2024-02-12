import uuid

from dateutil.relativedelta import relativedelta
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.languages.fields import LanguageField


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
        max_length=255,
        verbose_name=_("Nombres"),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_("Apellidos"),
    )

    class Meta:
        verbose_name = _("Autor")
        verbose_name_plural = _("Autores")

    def __str__(self):
        initials = "".join([name[0].upper() + "." for name in self.first_name.split()])
        return self.last_name + ", " + initials


class Classification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Clasificación"),
    )

    class Meta:
        verbose_name = _("Clasificación")
        verbose_name_plural = _("Clasificacións")

    def __str__(self):
        return self.name


class Source(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Fuente"),
    )

    class Meta:
        verbose_name = _("Fuente")
        verbose_name_plural = _("Fuentes")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Editorial"),
    )

    class Meta:
        verbose_name = _("Editorial")
        verbose_name_plural = _("Editoriales")

    def __str__(self):
        return self.name


class Collection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Colección"),
    )

    class Meta:
        verbose_name = _("Colección")
        verbose_name_plural = _("Colecciones")

    def __str__(self):
        return self.name


class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Facultad"),
    )

    class Meta:
        verbose_name = _("Facultad")
        verbose_name_plural = _("Facultades")

    def __str__(self):
        return self.name


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Escuela"),
    )
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, verbose_name=_("Facultad")
    )

    class Meta:
        verbose_name = _("Escuela")
        verbose_name_plural = _("Escuelas")

    def __str__(self):
        return self.name


class Career(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Carrera"),
    )
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name=_("Escuela")
    )

    class Meta:
        verbose_name = _("Carrera")
        verbose_name_plural = _("Carreras")

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Asignatura"),
    )
    career = models.ManyToManyField(Career, verbose_name=_("Carrera"))

    class Meta:
        verbose_name = _("Asignatura")
        verbose_name_plural = _("Asignaturas")

    def __str__(self):
        return self.name


class Theme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Tema"),
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name=_("Asignatura")
    )

    class Meta:
        verbose_name = _("Tema")
        verbose_name_plural = _("Temas")

    def __str__(self):
        return self.name


class License(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Licencia"),
    )
    image = models.ImageField(
        null=True, blank=True, upload_to="licenses", verbose_name=_("Imagen")
    )
    description = models.TextField(null=True, blank=True, verbose_name=_("Descripción"))
    url = models.URLField(null=True, blank=True, verbose_name=_("URL"))

    class Meta:
        verbose_name = _("Licencia")
        verbose_name_plural = _("Licencias")

    def __str__(self):
        return self.name


class Format(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Formato"),
    )

    class Meta:
        verbose_name = _("Formato")
        verbose_name_plural = _("Formatos")

    def __str__(self):
        return self.name


class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    international_id = models.CharField(
        max_length=255, unique=True, verbose_name=_("ID Internacional")
    )
    title = models.CharField(max_length=255, verbose_name=_("Título"))
    edition = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Edición")
    )
    author = models.ManyToManyField(Author, verbose_name=_("Autor"))
    publish_date = models.DateField(verbose_name=_("Fecha de Publicación"))
    coverage_start = models.DateField(verbose_name=_("Fecha de Inicio de Cobertura"))
    coverage_end = models.DateField(verbose_name=_("Fecha de Fin de Cobertura"))
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, verbose_name=_("Editorial")
    )
    abstract = models.TextField(verbose_name=_("Resumen"))
    extension = models.CharField(max_length=255, verbose_name=_("Extensión"))
    language = LanguageField(verbose_name=_("Idioma"))
    license = models.ForeignKey(
        License, on_delete=models.CASCADE, verbose_name=_("Licencia")
    )
    format = models.ManyToManyField(Format, verbose_name=_("Formato"))
    url = models.URLField(null=True, blank=True, verbose_name=_("URL"))
    location = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Ubicación")
    )
    adquisition_date = models.DateField(verbose_name=_("Fecha de Adquisición"))
    source = models.ForeignKey(
        Source, on_delete=models.CASCADE, verbose_name=_("Fuente")
    )
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE, verbose_name=_("Clasificación")
    )
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, verbose_name=_("Colección")
    )
    faculty = models.ManyToManyField(Faculty, verbose_name=_("Facultad"))
    school = models.ManyToManyField(School, verbose_name=_("Escuela"))
    career = models.ManyToManyField(Career, verbose_name=_("Carrera"))
    subject = models.ManyToManyField(Subject, verbose_name=_("Asignatura"))
    theme = models.ManyToManyField(Theme, verbose_name=_("Tema"))

    class Meta:
        verbose_name = _("Recurso")
        verbose_name_plural = _("Recursos")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("resource_detail", args=[str(self.pk)])

    def save(self, *args, **kwargs):
        self.international_id = self.international_id.upper()
        self.coverage_start = self.publish_date
        self.coverage_end = self.coverage_start + relativedelta(years=5)
        super().save(*args, **kwargs)
