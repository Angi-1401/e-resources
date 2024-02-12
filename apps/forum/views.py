from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from apps.accounts.models import User
from apps.forum.filters import ForumFilter, PostFilter
from apps.forum.models import Forum, Post, Reply, Comment
from apps.forum.tables import ForumHTMxTable, PostHTMxTable


class ForumListView(SingleTableMixin, FilterView):
    model = Forum
    table_class = ForumHTMxTable
    filterset_class = ForumFilter
    template_name = "forum/forum_table_htmx.html"
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "forum/table_partial.html"

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Forum.objects.all()


class PostListView(SingleTableMixin, FilterView):
    model = Post
    table_class = PostHTMxTable
    filterset_class = PostFilter
    template_name = "forum/post_table_htmx.html"
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "forum/table_partial.html"

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forum"] = Forum.objects.get(pk=self.kwargs.get("pk"))
        return context

    def get_queryset(self):
        forum = self.kwargs.get("pk")
        return Post.objects.filter(forum=forum)


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post"
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega tus formularios al contexto aquí
        return context
