# Generated by Django 2.2.4 on 2020-07-03 05:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0004_auto_20200702_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='hole',
            name='tee_black',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hole',
            name='tee_blue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hole',
            name='tee_gold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hole',
            name='tee_green',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hole',
            name='tee_red',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hole',
            name='tee_white',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Tee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yards', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('par', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('hole', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tees', to='golfapp.Hole')),
            ],
        ),
    ]