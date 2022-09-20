# Generated by Django 3.2.15 on 2022-09-20 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='project name', max_length=100, verbose_name='project name')),
                ('code', models.CharField(help_text='project code', max_length=10, verbose_name='project code')),
                ('description', models.TextField(help_text='project description', max_length=1000, verbose_name='project description')),
                ('creator', models.ForeignKey(blank=True, help_text='project creator', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_projects', to=settings.AUTH_USER_MODEL, verbose_name='project creator')),
                ('owner', models.ForeignKey(blank=True, help_text='project owner', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_projects', to=settings.AUTH_USER_MODEL, verbose_name='project owner')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ProjectTaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='status name', max_length=15, verbose_name='status name')),
                ('project', models.ForeignKey(help_text='related project', on_delete=django.db.models.deletion.CASCADE, related_name='task_statuses', to='projects.project', verbose_name='related project')),
            ],
            options={
                'verbose_name': 'ProjectTaskStatus',
                'verbose_name_plural': 'ProjectTaskStatus',
                'ordering': ('id',),
            },
        ),
    ]
