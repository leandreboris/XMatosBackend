# Generated by Django 3.2.6 on 2021-08-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0003_rename_object_id_objectviewed_article_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectviewed',
            name='article_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
