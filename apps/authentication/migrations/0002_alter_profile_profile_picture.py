# Generated by Django 3.2.6 on 2024-01-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/assets/img/profile_pic.jpg', null=True, upload_to=''),
        ),
    ]
