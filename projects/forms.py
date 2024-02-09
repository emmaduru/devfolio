from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ("thumbnail", "name", "description", "skills", "kaggle", "github", "website", "type",)
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "skills": forms.Textarea(attrs={"rows": 5})
        }
        labels={
            "skills": "Skills (Enter skills separated by commas)",
        }