# Generated by Django 3.2.6 on 2021-08-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_rename_is_activated_user_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_provider',
            field=models.CharField(default='email', max_length=255),
        ),
    ]