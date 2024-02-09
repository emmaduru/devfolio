# Generated by Django 5.0.2 on 2024-02-06 22:15

import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='github',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[users.validators.validate_github]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='kaggle',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[users.validators.validate_kaggle]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='linkedin',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[users.validators.validate_linkedin]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='medium',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[users.validators.validate_medium]),
        ),
    ]