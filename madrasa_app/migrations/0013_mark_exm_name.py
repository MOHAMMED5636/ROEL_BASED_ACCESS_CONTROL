# Generated by Django 5.0.1 on 2024-03-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa_app', '0012_remove_user_class_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='Exm_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
