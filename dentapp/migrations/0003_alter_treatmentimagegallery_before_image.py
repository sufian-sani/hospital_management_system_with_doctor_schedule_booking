# Generated by Django 4.0.4 on 2022-05-09 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentapp', '0002_rename_image_treatmentimagegallery_after_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentimagegallery',
            name='before_image',
            field=models.ImageField(upload_to='TreatmentImageGallery'),
        ),
    ]
