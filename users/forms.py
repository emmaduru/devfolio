from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email", "password1", "password2",)

class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("photo", "headline", "location", "about", "skills", "github", "linkedin", "kaggle", "medium")
        widgets = {
            "about": forms.Textarea(attrs={"rows": 5}),
            "skills": forms.Textarea(attrs={"rows": 5})
        }
        labels={
            "skills": "Skills (Enter skills separated by commas)",
            "headline": "Headline (Current role)"
        }