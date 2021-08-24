from django.db import models
from Users.models import User






# Categorie model, following the class diagramm specifications

class Categorie(models.Model):
    libelle = models.CharField(max_length=256)

    def __str__(self):
        return self.libelle



# Mode de livraison model, following the class diagramm specifications
class ModeDeLivraison(models.Model):
    libelle = models.CharField(max_length=50)
    description= models.CharField(max_length=256)

    def __str__(self):
        return self.libelle


# Mode de paiement model, following the class diagramm specifications
class ModeDePaiement(models.Model):
    libelle = models.CharField(max_length=50)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.libelle




# Commande model, following the class diagramm specifications
class Commande(models.Model):
    modeDeLivraison = models.ForeignKey(ModeDeLivraison, on_delete=models.CASCADE)
    modeDePaiement = models.ForeignKey(ModeDePaiement, on_delete=models.CASCADE)
    dateAjout = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.dateAjout)

    class Meta:
        ordering = ['dateAjout']


# Facture model, following the class diagramm specifications
class Facture(models.Model):
    date_bought = models.DateTimeField(auto_now_add=True)
    ht_price = models.FloatField()
    total_ht = models.FloatField()
    total_ttc = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return "Facture de " + str(self.date_bought)

    class Meta:
        ordering = ['date_bought']


# Article model, following the class diagramm specifications
class Article(models.Model):
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    location = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
