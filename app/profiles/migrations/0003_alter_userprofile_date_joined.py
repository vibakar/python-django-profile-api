# Generated by Django 5.0.6 on 2024-06-26 19:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_date_joined_userprofile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]