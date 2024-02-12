from django.urls import path

from apps.library import views

urlpatterns = [
    path("", views.ResourceListView.as_view(), name="resource_list"),
    path("<uuid:pk>/", views.ResourceDetail.as_view(), name="resource_detail"),
]
