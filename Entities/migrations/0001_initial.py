# Generated by Django 3.2.6 on 2021-08-10 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('idCategorie', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('libelleCategorie', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ModeDeLivraison',
            fields=[
                ('idModeDeLivraison', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('libelleModeDeLivraison', models.CharField(max_length=50)),
                ('descriptionModeDeLivraison', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ModeDePaiement',
            fields=[
                ('idModeDePaiement', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('libelleModeDePaiement', models.CharField(max_length=50)),
                ('descriptionModeDePaiement', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('idFacture', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('datePaiementFacture', models.DateTimeField(auto_now_add=True)),
                ('prixHtFacture', models.FloatField()),
                ('totalHtFacture', models.FloatField()),
                ('totalTtc', models.FloatField()),
                ('clientFacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('idCommande', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('dateAjoutCommande', models.DateTimeField(auto_now_add=True)),
                ('descriptionCommande', models.CharField(max_length=256)),
                ('modeDeLivraisonCommande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entities.modedelivraison')),
                ('modeDePaiementCommande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entities.modedepaiement')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('idArticle', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('imageArticle', models.ImageField(blank=True, null=True, upload_to='')),
                ('nomArticle', models.CharField(max_length=50)),
                ('descriptionArticle', models.CharField(max_length=256)),
                ('quantiteArticle', models.IntegerField()),
                ('prixArticle', models.FloatField()),
                ('dateAjoutArticle', models.DateTimeField(auto_now_add=True)),
                ('categorieArticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entities.categorie')),
            ],
        ),
    ]
