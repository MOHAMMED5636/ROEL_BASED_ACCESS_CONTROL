# Generated by Django 5.0.1 on 2024-03-18 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa_app', '0009_claass_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claass_no',
            name='admin',
        ),
    ]