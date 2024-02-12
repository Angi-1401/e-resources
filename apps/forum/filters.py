import django_filters as filters

from django import forms

from apps.forum.models import Forum, Post


class ForumFilter(filters.FilterSet):
    resource__title = filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Busca por título y presiona ENTER"}
        ),
    )

    class Meta:
        model = Forum
        fields = ["resource__title"]


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Busca por título y presiona ENTER"}
        ),
    )

    class Meta:
        model = Post
        fields = ["title"]
