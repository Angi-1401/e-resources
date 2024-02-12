from django.urls import path

from apps.forum import views

urlpatterns = [
    path("", views.ForumListView.as_view(), name="forum_list"),
    path("<uuid:forum>/", views.PostListView.as_view(), name="post_list"),
    path("<uuid:forum>/<uuid:post>/", views.PostDetailView.as_view(), name="post_detail"),
]
