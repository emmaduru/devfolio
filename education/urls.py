from django.urls import path
from .views import EducationCreateView, EducationUpdateView, EducationDeleteView

urlpatterns = [
    path("add/", EducationCreateView.as_view(), name="education_add"),
    path("<slug:slug>/edit/", EducationUpdateView.as_view(), name="education_edit"),
    path("<slug:slug>/delete/", EducationDeleteView.as_view(), name="education_delete")
]