# Generated by Django 5.0.1 on 2024-03-18 08:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa_app', '0007_leave_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('result', models.ImageField(blank=True, null=True, upload_to='result/')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_result', to=settings.AUTH_USER_MODEL, verbose_name='student_result')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_result', to=settings.AUTH_USER_MODEL, verbose_name='teacher_result')),
            ],
        ),
    ]
