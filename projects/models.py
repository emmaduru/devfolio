import cloudinary
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from  .validators import validate_github, validate_kaggle, validate_website

TYPES = (
    ("Frontend", "Frontend"),
    ("Backend", "Backend"),
    ("Fullstack", "Fullstack"),
    ("Mobile", "Mobile"),
    ("Game", "Game"),
    ("Data Analytics", "Data Analytics")
)

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="images/", default="project-img.webp")
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    skills = models.TextField()
    github = models.CharField(max_length=255, null=True, blank=True, validators=[validate_github])
    kaggle = models.CharField(max_length=255, null=True, blank=True, validators=[validate_kaggle])
    website = models.CharField(max_length=255, null=True, blank=True, validators=[validate_website])
    type = models.CharField(max_length=15, choices=TYPES, default="Fullstack")
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        if self.github and not self.github.startswith("https://"):
            self.github = f"https://{self.github}"

        if self.kaggle and not self.kaggle.startswith("https://"):
            self.kaggle = f"https://{self.kaggle}"

        if self.website and not self.website.startswith("https://"):
            self.website = f"https://{self.website}"
            
        super().save(*args, **kwargs)

@receiver(pre_delete, sender=Project)
def thumbnail_delete(sender, instance, **kwargs):
    thumbnail = str(instance.thumbnail)
    cloudinary.uploader.destroy(thumbnail)
