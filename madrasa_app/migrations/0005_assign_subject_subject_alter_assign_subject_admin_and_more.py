# Generated by Django 5.0.1 on 2024-03-14 06:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa_app', '0004_assign_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign_subject',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_subject', to='madrasa_app.subject', verbose_name='Assigned Subject'),
        ),
        migrations.AlterField(
            model_name='assign_subject',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_admin', to=settings.AUTH_USER_MODEL, verbose_name='Assigning Admin'),
        ),
        migrations.AlterField(
            model_name='assign_subject',
            name='class_no',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Class Number'),
        ),
        migrations.AlterField(
            model_name='assign_subject',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_teacher', to=settings.AUTH_USER_MODEL, verbose_name='Assigned Teacher'),
        ),
    ]
