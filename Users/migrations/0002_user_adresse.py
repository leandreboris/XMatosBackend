# Generated by Django 3.2.6 on 2021-08-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adresse',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]