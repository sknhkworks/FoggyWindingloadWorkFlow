# Generated by Django 5.0.2 on 2024-02-23 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelfs',
            name='parent',
        ),
    ]
