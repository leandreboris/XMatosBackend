from django.db import models


# Facture model, following the class diagramm specifications
class Facture(models.Model):
    date_bought = models.DateTimeField(auto_now_add=True)
    ht_price = models.FloatField()
    total_ht = models.FloatField()
    total_ttc = models.FloatField()


    def __str__(self):
        return "Facture de " + str(self.date_bought)




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

    def __str__(self):
        return self.dateAjout


