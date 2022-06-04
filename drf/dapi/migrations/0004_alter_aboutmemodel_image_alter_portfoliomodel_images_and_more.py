# Generated by Django 4.0 on 2022-02-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapi', '0003_remove_contactmodel_phone_contactmodel_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmemodel',
            name='image',
            field=models.ImageField(height_field=250, upload_to='about/images/', width_field=250),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='images',
            field=models.ImageField(height_field=350, upload_to='portfolio/images/', width_field=400),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='thumbnail',
            field=models.ImageField(height_field=250, upload_to='portfolio/images/', width_field=250),
        ),
    ]
