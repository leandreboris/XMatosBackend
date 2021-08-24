from django.contrib import admin
from .models import *


# Register your models here.


# Registrations of all models
admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(ModeDeLivraison)
admin.site.register(ModeDePaiement)
admin.site.register(Commande)
admin.site.register(Facture)


