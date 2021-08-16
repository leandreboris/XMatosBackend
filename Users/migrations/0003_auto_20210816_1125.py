# Generated by Django 3.2.6 on 2021-08-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_user_adresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_local',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_ip',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
