import django_tables2 as tables

from apps.library.models import Resource


class ResourceHTMxTable(tables.Table):
    title = tables.LinkColumn(args=[tables.A("pk")])
    paginator_class = tables.LazyPaginator

    class Meta:
        model = Resource
        template_name = "library/bootstrap5_htmx.html"
        fields = ("publish_date", "title", "author")
        order_by = ("-publish_date",)
