# Generated by Django 2.2.4 on 2020-07-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0005_auto_20200702_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hole',
            name='tee_black',
        ),
        migrations.RemoveField(
            model_name='hole',
            name='tee_blue',
        ),
        migrations.RemoveField(
            model_name='hole',
            name='tee_gold',
        ),
        migrations.RemoveField(
            model_name='hole',
            name='tee_green',
        ),
        migrations.RemoveField(
            model_name='hole',
            name='tee_red',
        ),
        migrations.RemoveField(
            model_name='hole',
            name='tee_white',
        ),
        migrations.AddField(
            model_name='course',
            name='tee_black',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='tee_blue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='tee_gold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='tee_green',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='tee_red',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='tee_white',
            field=models.BooleanField(default=False),
        ),
    ]
