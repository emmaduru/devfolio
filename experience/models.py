from datetime import date
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

year = int(date.today().year)

# Create your models here.
class Experience(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    from_date = models.IntegerField(validators=[MinValueValidator(1960), MaxValueValidator(year)])
    to_date = models.IntegerField(validators=[MinValueValidator(1960), MaxValueValidator(year)])
    role = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.role
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.user.username} {self.role}")
        super().save(*args, **kwargs)