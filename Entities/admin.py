from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    



admin.site.register(User, AccountAdmin)
admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(ModeDeLivraison)
admin.site.register(ModeDePaiement)
admin.site.register(Commande)
admin.site.register(Facture)