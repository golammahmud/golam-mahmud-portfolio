# Generated by Django 4.0 on 2022-02-25 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapi', '0002_aboutmemodel_contactmodel_homepagemodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='phone',
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
