from rest_framework import serializers
from Entities.models import *


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = (
            'id',
            'libelle',
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
            'libelle',
            'description',
        )


class ModeDePaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeDePaiement
        fields = (
            'id',
            'libelle',
            'description',
        )

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = (
            'id',
            'modeDeLivraison',
            'modeDePaiement',
            'dateAjout',
            'description',
            
        )

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = (
            'id',
            'date_bought',
            'ht_price',
            'total_ht', 
            'total_ttc',
            
        )