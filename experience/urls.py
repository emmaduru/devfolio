from django.urls import path
from .views import ExperienceCreateView, ExperienceUpdateView, ExperienceDeleteView

urlpatterns = [
    path("add/", ExperienceCreateView.as_view(), name="experience_add"),
    path("<slug:slug>/edit/", ExperienceUpdateView.as_view(), name="experience_edit"),
    path("<slug:slug>/delete/", ExperienceDeleteView.as_view(), name="experience_delete")
]