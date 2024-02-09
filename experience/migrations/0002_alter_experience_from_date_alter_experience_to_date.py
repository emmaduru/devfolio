# Generated by Django 5.0.2 on 2024-02-07 10:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='from_date',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1960), django.core.validators.MaxValueValidator(2024)]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1960), django.core.validators.MaxValueValidator(2024)]),
        ),
    ]
