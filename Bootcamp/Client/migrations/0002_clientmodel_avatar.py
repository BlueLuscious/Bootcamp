# Generated by Django 4.2.4 on 2023-08-22 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientmodel',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatar'),
        ),
    ]
