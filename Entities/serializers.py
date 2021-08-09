from rest_framework import serializers
from Entities.models import *


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = (
            'idCategorie',
            'libelleCategorie',
        )

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'idArticle',
            'imageArticle',
            'categorieArticle',
            'nomArticle',
            'descriptionArticle',
            'quantiteArticle',
            'prixArticle',
            'dateAjoutArticle',
        )


class ModeDeLivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeDeLivraison
        fields = (
            'idModeDeLivraison',
            'libelleModeDeLivraison',
            'descriptionModeDeLivraison',
        )


class ModeDePaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeDePaiement
        fields = (
            'idModeDePaiement',
            'libelleModeDePaiement',
            'descriptionModeDePaiement',
        )

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = (
            'idCommande',
            'modeDeLivraisonCommande',
            'modeDePaiementCommande',
            'dateAjoutCommande',
            'descriptionCommande',
            
        )

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = (
            'idFacture',
            'clientFacture',
            'datePaiementFacture',
            'prixHtFacture',
            'totalHtFacture', 
            'totalTtc',
            
        )