from django.db import models
from Users.models import User 




# Categorie model, following the class diagramm specifications

class Categorie(models.Model):
    libelleCategorie = models.CharField(max_length=256)

    def __str__(self):
        return self.libelleCategorie

    
    



# Article model, following the class diagramm specifications
class Article(models.Model):
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    quantity = models.IntegerField()
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





# Mode de livraison model, following the class diagramm specifications
class ModeDeLivraison(models.Model):
    libelleModeDeLivraison = models.CharField(max_length=50)
    descriptionModeDeLivraison = models.CharField(max_length=256)

    def __str__(self):
        return self.libelleModeDeLivraison


# Mode de paiement model, following the class diagramm specifications
class ModeDePaiement(models.Model):
    libelleModeDePaiement = models.CharField(max_length=50)
    descriptionModeDePaiement = models.CharField(max_length=256)

    def __str__(self):
        return self.libelleModeDePaiement


# Commande model, following the class diagramm specifications
class Commande(models.Model):
    modeDeLivraisonCommande = models.ForeignKey(ModeDeLivraison, on_delete=models.CASCADE)
    modeDePaiementCommande = models.ForeignKey(ModeDePaiement, on_delete=models.CASCADE)
    dateAjoutCommande = models.DateTimeField(auto_now_add=True)
    descriptionCommande = models.CharField(max_length=256)

    def __str__(self):
        return self.dateAjoutCommande



# Facture model, following the class diagramm specifications
class Facture(models.Model):
    clientFacture  = models.ForeignKey(User, on_delete=models.CASCADE)
    datePaiementFacture = models.DateTimeField(auto_now_add=True)
    prixHtFacture = models.FloatField()
    totalHtFacture = models.FloatField()
    totalTtc = models.FloatField()

    def __str__(self):
        return "Facture de " + str(self.clientFacture)


