# Generated by Django 5.0.1 on 2024-03-18 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa_app', '0010_remove_claass_no_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='class_rooom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_room', to='madrasa_app.claass_no', verbose_name='class_room'),
        ),
    ]
