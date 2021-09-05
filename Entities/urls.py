from Entities import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [


    url(r'^categories$', views.categorieApi_list),
    url(r'^categories/([0-9]+)$', views.categorieApi_details),

    url(r'^articles$', views.articleApi_list),
    url(r'^articles/([0-9]+)$', views.articleApi_details),

    url(r'^livraisons$', views.modeDeLivraisonApi_list),
    url(r'^livraisons/([0-9]+)$', views.modeDeLivraisonApi_details),

    url(r'^paiements$', views.modeDePaiementApi_list),
    url(r'^paiements/([0-9]+)$', views.modeDePaiementApi_details),

    url(r'^factures$', views.factureApi_list),
    url(r'^factures/([0-9]+)$', views.factureApi_details),

    url(r'^commandes$', views.commandeApi_list),
    url(r'^commandes/([0-9]+)$', views.commandeApi_details),

]

urlpatterns = format_suffix_patterns(urlpatterns)
