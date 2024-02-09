from django import forms

from .models import Education

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ("degree", "school", "from_date", "to_date", "description",)
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "from_date": "From year",
            "to_date": "To year"
        }