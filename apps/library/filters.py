import django_filters as filters
import string

from django import forms
from django.db.models import Q

from apps.library.models import (
    Collection,
    Faculty,
    School,
    Career,
    Subject,
    Theme,
    Resource,
)


class ResourceFilter(filters.FilterSet):
    title = filters.CharFilter(
        label="",
        method="universal_search",
        widget=forms.TextInput(
            attrs={"placeholder": "Busca por título y presiona ENTER"}
        ),
    )
    author = filters.ChoiceFilter(
        label="Autor",
        choices=[(letter, letter) for letter in string.ascii_uppercase],
        method="filter_by_letter",
    )
    publish_date = filters.NumberFilter(
        field_name="publish_date__year", label="Año de publicación", lookup_expr="exact"
    )
    collection = filters.ModelChoiceFilter(
        queryset=Collection.objects.all().order_by("name"),
        field_name="collection__name",
        label="Colección",
    )
    faculty = filters.ModelMultipleChoiceFilter(
        queryset=Faculty.objects.all().order_by("name"),
        field_name="faculty__name",
        label="Facultad",
    )
    school = filters.ModelMultipleChoiceFilter(
        queryset=School.objects.all().order_by("name"),
        field_name="school__name",
        label="Escuela",
    )
    career = filters.ModelMultipleChoiceFilter(
        queryset=Career.objects.all().order_by("name"),
        field_name="career__name",
        label="Carrera",
    )
    subject = filters.ModelMultipleChoiceFilter(
        queryset=Subject.objects.all().order_by("name"),
        field_name="subject__name",
        label="Asignatura",
    )
    theme = filters.ModelMultipleChoiceFilter(
        queryset=Theme.objects.all().order_by("name"),
        field_name="theme__name",
        label="Tema",
    )

    class Meta:
        model = Resource
        fields = (
            "title",
            "author",
            "publish_date",
            "collection",
            "faculty",
            "school",
            "career",
            "subject",
            "theme",
        )

    def universal_search(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value))

    def filter_by_author(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author__last_name__istartswith=value)
        return queryset
