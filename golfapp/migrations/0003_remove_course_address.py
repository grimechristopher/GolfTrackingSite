# Generated by Django 2.2.4 on 2020-07-03 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0002_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='address',
        ),
    ]