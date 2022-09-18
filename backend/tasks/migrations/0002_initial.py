# Generated by Django 3.2.15 on 2022-09-18 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='taskloggedtime',
            name='user',
            field=models.ForeignKey(help_text='executor', on_delete=django.db.models.deletion.CASCADE, related_name='logged_time', to=settings.AUTH_USER_MODEL, verbose_name='executor'),
        ),
        migrations.AddField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(help_text='task creator', on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to=settings.AUTH_USER_MODEL, verbose_name='task creator'),
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(help_text='task executor', on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='task executor'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(help_text='related project', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.project', verbose_name='related project'),
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(blank=True, help_text='project creator', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_projects', to=settings.AUTH_USER_MODEL, verbose_name='project creator'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='project owner', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_projects', to=settings.AUTH_USER_MODEL, verbose_name='project owner'),
        ),
    ]
