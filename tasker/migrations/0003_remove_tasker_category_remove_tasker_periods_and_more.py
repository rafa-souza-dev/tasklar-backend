# Generated by Django 5.0.1 on 2024-07-10 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0002_alter_tasker_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasker',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tasker',
            name='periods',
        ),
        migrations.RemoveField(
            model_name='tasker',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tasker',
            name='hourly_rate',
        ),
        migrations.RemoveField(
            model_name='tasker',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Period',
        ),
    ]
