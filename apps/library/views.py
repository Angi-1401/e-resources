from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from apps.library.filters import ResourceFilter
from apps.library.models import Resource
from apps.library.tables import ResourceHTMxTable


class ResourceListView(SingleTableMixin, FilterView):
    model = Resource
    table_class = ResourceHTMxTable
    filterset_class = ResourceFilter
    template_name = "library/resource_table_htmx.html"
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "library/table_partial.html"

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Resource.objects.all()


class ResourceDetail(DetailView):
    model = Resource
    template_name = "library/resource_detail.html"
    context_object_name = "resource"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uuid = self.kwargs.get("pk")
        context["id"] = uuid

        resource = context["resource"]

        if resource.career.exists():
            career = resource.career.first()
            context["career"] = career.name

            if career.school:
                context["school"] = career.school.name

                if career.school.faculty:
                    context["faculty"] = career.school.faculty.name

        if resource.format.exists():
            context["formats"] = resource.format.all()

        return context
