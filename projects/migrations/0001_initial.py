# Generated by Django 5.0.2 on 2024-02-07 00:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(default='project-img.jpeg', upload_to='images/')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('skills', models.TextField()),
                ('github', models.CharField(blank=True, max_length=255, null=True)),
                ('kaggle', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack'), ('Mobile', 'Mobile'), ('Game', 'Game'), ('Data Analytics', 'Data Analytics')], default='Fullstack', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
