# Generated by Django 5.0.1 on 2024-03-19 03:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa_app', '0013_mark_exm_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_rele', to=settings.AUTH_USER_MODEL, verbose_name='parent_rele')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studet_rele', to=settings.AUTH_USER_MODEL, verbose_name='studet_rele')),
            ],
        ),
    ]
