from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .forms import ProjectForm
from .models import Project

# Create your views here.
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/add.html"
    success_url = reverse_lazy("dashboard")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add"
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skills"] = [skill.strip() for skill in self.get_object().skills.split(",")]
        return context
    
class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = self.get_queryset().order_by("-id")
        context["projects"] = projects
        context["frontend_projects"] = projects.filter(type="Frontend")
        context["backend_projects"] = projects.filter(type="Backend")
        context["fullstack_projects"] = projects.filter(type="Fullstack")
        context["mobile_projects"] = projects.filter(type="Mobile")
        context["game_projects"] = projects.filter(type="Game")
        context["data_projects"] = projects.filter(type="Data Analytics")
        return context 

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/add.html"
    success_url = reverse_lazy("dashboard")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit"
        return context

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    http_method_names = ["post"]
    model = Project
    success_url = reverse_lazy("dashboard")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user