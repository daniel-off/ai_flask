# Generated by Django 3.1.7 on 2021-04-04 05:35

from django.db import migrations, models
import django_app.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210404_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(storage=django_app.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]
