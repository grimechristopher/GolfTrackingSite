# Generated by Django 2.2.4 on 2020-07-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0013_auto_20200703_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, choices=[('WHITE', 'White'), ('RED', 'Red'), ('BLUE', 'Blue'), ('GREEN', 'Green'), ('BLACK', 'Black'), ('GOLD', 'Gold')], max_length=255, null=True)),
            ],
        ),
    ]
