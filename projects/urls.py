from django.urls import path
from .views import ProjectCreateView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView, ProjectListView

urlpatterns = [
    path("add/", ProjectCreateView.as_view(), name="project_add"),
    path("<slug:slug>/edit/", ProjectUpdateView.as_view(), name="project_edit"),
    path("<slug:slug>/delete/", ProjectDeleteView.as_view(), name="project_delete"),
    path("<slug:slug>/", ProjectDetailView.as_view(), name="project_detail"),
    path("", ProjectListView.as_view(), name="project_list")
]