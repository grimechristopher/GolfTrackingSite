# Generated by Django 2.2.4 on 2020-07-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0008_auto_20200703_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='golferuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=255, null=True),
        ),
    ]
