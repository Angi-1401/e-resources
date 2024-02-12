import django_tables2 as tables

from django.urls import reverse

from apps.forum.models import Forum, Post


class ForumHTMxTable(tables.Table):
    resource = tables.LinkColumn(
        verbose_name="Recurso",
        accessor="resource.title",
        args=[tables.A("id")],
        viewname="post_list",
    )
    post_count = tables.Column(
        verbose_name="Publicaciones totales", accessor="get_posts.count"
    )
    last_post_date = tables.Column(
        verbose_name="Últ. Publicación", accessor="last_post.timestamp"
    )
    paginator_class = tables.LazyPaginator

    class Meta:
        model = Forum
        template_name = "forum/bootstrap5_htmx.html"
        fields = ("resource", "post_count", "last_post_date")
        order_by = "resource"


class PostHTMxTable(tables.Table):
    title = tables.LinkColumn(
        verbose_name="Título",
        accessor="title",
        args=[tables.A("forum.id")],
    )
    user = tables.Column(
        verbose_name="Usuario",
        accessor="user.username",
    )

    class Meta:
        model = Post
        template_name = "forum/bootstrap5_htmx.html"
        fields = ("title", "user", "timestamp")
        order_by = "timestamp"
