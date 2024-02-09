from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Experience
from .forms import ExperienceForm

# Create your views here.
class ExperienceCreateView(LoginRequiredMixin, CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = "experience/add.html"
    success_url = reverse_lazy("dashboard")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add"
        return context
    
class ExperienceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = "experience/add.html"
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

class ExperienceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    http_method_names = ["post"]
    model = Experience
    success_url = reverse_lazy("dashboard")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user