from rest_framework import serializers
from Entities.models import *


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = (
            'id',
            'libelleCategorie',
        )

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'image',
            'category',
            'name',
            'description',
            'quantity',
            'price',
            'date_added',
        )


class ModeDeLivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeDeLivraison
        fields = (
            'id',
            'libelleModeDeLivraison',
            'descriptionModeDeLivraison',
        )


class ModeDePaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeDePaiement
        fields = (
            'id',
            'libelleModeDePaiement',
            'descriptionModeDePaiement',
        )

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = (
            'id',
            'modeDeLivraisonCommande',
            'modeDePaiementCommande',
            'dateAjoutCommande',
            'descriptionCommande',
            
        )

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = (
            'id',
            'clientFacture',
            'datePaiementFacture',
            'prixHtFacture',
            'totalHtFacture', 
            'totalTtc',
            
        )