# Generated by Django 3.2.12 on 2022-05-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20220522_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientschedule',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
