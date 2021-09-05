from .models import *
from .serializers import *


from django.http.response import JsonResponse
from django.contrib.auth import login



from rest_framework.parsers import  JSONParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from Entities.permissions import IsAdminOrReadOnly, IsProviderOrReadOnly
from Analytics.signals import object_viewed_signal








"""                             REST APIs for required entities                      """

# Categorie API
@api_view(['GET', 'POST',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminOrReadOnly])
def categorieApi_list(request, format=None):
    """
    List all categories, or create a new categorie of products.

    """
    if request.method == 'GET':
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminOrReadOnly])
def categorieApi_details(request, id, format=None):
    """
    Get, update or delete a categorie of products.

    """
    try:
        categorie = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        categorie_serializer = CategorieSerializer(categorie)
        return Response(categorie_serializer.data)

    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = CategorieSerializer(categorie, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        categorie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Article API

@api_view(['GET', 'POST', ])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsProviderOrReadOnly])
def articleApi_list(request, format=None):
    """
    List all articles, or create a new article.

    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsProviderOrReadOnly])
def articleApi_details(request, id, format=None):
    """
    Get, update or delete a categorie of products.

    """
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        article_serializer = ArticleSerializer(article)
        object_viewed_signal.send(Article, instanceID=id, request=request)
        return Response(article_serializer.data)

    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Mode de livraison API
@api_view(['GET', 'POST', ])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def modeDeLivraisonApi_list(request, format=None):
    """
    List all modes, or create a new mode.

    """
    if request.method == 'GET':
        livraisons = ModeDeLivraison.objects.all()
        serializer = ModeDeLivraisonSerializer(livraisons, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ModeDeLivraisonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminOrReadOnly])
def modeDeLivraisonApi_details(request, id, format=None):
    """
    Get, update or delete a delivery mode of products.

    """
    try:
        mode = ModeDeLivraison.objects.get(id=id)
    except ModeDeLivraison.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        mode_serializer = ModeDeLivraisonSerializer(mode)
        return Response(mode_serializer.data)

    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = ModeDeLivraison(mode, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        mode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# Mode de paiement API
@api_view(['GET', 'POST',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def modeDePaiementApi_list(request, format=None):
    """
    List all modes, or create a new mode.

    """
    if request.method == 'GET':
        paiements = ModeDePaiement.objects.all()
        serializer = ModeDePaiementSerializer(paiements, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ModeDePaiementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminOrReadOnly])
def modeDePaiementApi_details(request, id, format=None):
    """
    Get, update or delete a payment mode of products.

    """
    try:
        mode = ModeDePaiement.objects.get(id=id)
    except ModeDePaiement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        mode_serializer = ModeDePaiementSerializer(mode)
        return Response(mode_serializer.data)

    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = ModeDePaiementSerializer(mode, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        mode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Facture API
@api_view(['GET', 'POST',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def factureApi_list(request, format=None):
    """
    List all modes, or create a new mode.

    """
    if request.method == 'GET':
        factures = Facture.objects.all()
        serializer = FactureSerializer(factures, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FactureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminOrReadOnly])
def factureApi_details(request, id, format=None):
    """
    Get, update or delete a facture.

    """
    try:
        facture = Facture.objects.get(id=id)
    except Facture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        facture_serializer = Facture(facture)
        return Response(facture_serializer.data)

    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = FactureSerializer(facture, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        facture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Commande API
@api_view(['GET', 'POST',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def commandeApi_list(request, format=None):
    """
    List all modes, or create a new commande.

    """
    if request.method == 'GET':
        commandes = Commande.objects.all()
        serializer = CommandeSerializer(commandes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommandeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE',])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def commandeApi_details(request, id, format=None):
    """
    Get, update or delete a commande.

    """
    try:
        commande = Commande.objects.get(id=id)
    except Commande.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        commande_serializer = CommandeSerializer(commande)
        return Response(commande_serializer.data)

    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = CommandeSerializer(commande, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        commande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
