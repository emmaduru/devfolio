import cloudinary
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from .validators import validate_github, validate_kaggle, validate_linkedin, validate_medium

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    photo = models.ImageField(upload_to="images/", default="default.png")
    headline = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField()
    skills = models.TextField()
    github = models.CharField(max_length=255, null=True, blank=True, validators=[validate_github])
    linkedin = models.CharField(max_length=255, null=True, blank=True, validators=[validate_linkedin])
    kaggle = models.CharField(max_length=255, null=True, blank=True, validators=[validate_kaggle])
    medium = models.CharField(max_length=255, null=True, blank=True, validators=[validate_medium])
    slug = models.SlugField(unique=True, null=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        self.full_name = f"{self.first_name} {self.last_name}"

        if self.github and not self.github.startswith("https://"):
            self.github = f"https://{self.github}"

        if self.linkedin and not self.linkedin.startswith("https://"):
            self.linkedin = f"https://{self.linkedin}"

        if self.kaggle and not self.kaggle.startswith("https://"):
            self.kaggle = f"https://{self.kaggle}"

        if self.medium and not self.medium.startswith("https://"):
            self.medium = f"https://{self.medium}"

        super().save(*args, **kwargs)

# Delete image from cloudinary when model is deleted
@receiver(pre_delete, sender=CustomUser)
def photo_delete(sender, instance, **kwargs):
    photo = str(instance.photo)
    cloudinary.uploaded.destroy(photo)