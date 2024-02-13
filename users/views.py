from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from projects.models import Project
from experience.models import Experience
from education.models import Education
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "profile/profile_edit.html"
    success_url = reverse_lazy("dashboard")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user.username
    

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "profile/dashboard.html"
    login_url = "login"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = CustomUser.objects.filter(slug=self.request.user.slug)[0]
        context["skills"] = [skill.strip() for skill in context["user"].skills.split(",")]
        context["projects"] = Project.objects.filter(user=self.request.user).order_by("-id")
        context["experiences"] = Experience.objects.filter(user=self.request.user).order_by("-id")
        context["education"] = Education.objects.filter(user=self.request.user).order_by("-id")
        return context

class PortfolioView(DetailView):
    model = CustomUser
    template_name = "profile/portfolio.html"
    context_object_name = "profile"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["skills"] = [skill.strip() for skill in user.skills.split(",")]
        context["projects"] = Project.objects.filter(user=user).order_by("-id")
        context["experiences"] = Experience.objects.filter(user=user).order_by("-id")
        context["education"] = Education.objects.filter(user=user).order_by("-id")
        return context


def csrf_failure(request, reason=""):
    return render(request, "403.html")