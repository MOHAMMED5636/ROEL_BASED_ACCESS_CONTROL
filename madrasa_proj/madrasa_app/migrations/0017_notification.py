# Generated by Django 5.0.1 on 2024-03-20 06:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa_app', '0016_alter_attendance_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_notification', to=settings.AUTH_USER_MODEL, verbose_name='admin_notification')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_notification', to=settings.AUTH_USER_MODEL, verbose_name='teacher_notification')),
            ],
        ),
    ]
