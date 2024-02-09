from django import forms

from .models import Experience

class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ("role", "organization", "from_date", "to_date", "description",)
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "from_date": "From year",
            "to_date": "To year"
        }