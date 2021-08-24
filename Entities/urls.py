from Entities import views
from django.conf.urls import url


urlpatterns = [


    url(r'^categories$', views.categorieApi),
    url(r'^categories/([0-9]+)$', views.categorieApi),

    url(r'^articles$', views.articleApi),
    url(r'^articles/([0-9]+)$', views.articleApi),

    url(r'^livraisons$', views.modedelivraisonApi),
    url(r'^livraisons/([0-9]+)$', views.modedelivraisonApi),

    url(r'^paiements$', views.modedepaiementApi),
    url(r'^paiements/([0-9]+)$', views.modedepaiementApi),

    url(r'^factures$', views.factureApi),
    url(r'^factures/([0-9]+)$', views.factureApi),

    url(r'^commandes$', views.commandeApi),
    url(r'^commandes/([0-9]+)$', views.commandeApi),



]