# Generated by Django 3.2.6 on 2021-08-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_user_factures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='factures',
        ),
        migrations.AddField(
            model_name='user',
            name='factures',
            field=models.ManyToManyField(blank=True, null=True, to='Users.Facture'),
        ),
    ]