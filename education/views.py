from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Education
from .forms import EducationForm

# Create your views here.
class EducationCreateView(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = "education/add.html"
    success_url = reverse_lazy("dashboard")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add"
        return context
    
class EducationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Education
    form_class = EducationForm
    template_name = "education/add.html"
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

class EducationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    http_method_names = ["post"]
    model = Education
    success_url = reverse_lazy("dashboard")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user