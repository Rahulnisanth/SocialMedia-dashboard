# Generated by Django 3.2.6 on 2024-01-21 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram_manager', '0004_auto_20240121_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instagram',
            name='main_user',
        ),
        migrations.AddField(
            model_name='instagram',
            name='main_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instagram', to=settings.AUTH_USER_MODEL),
        ),
    ]
