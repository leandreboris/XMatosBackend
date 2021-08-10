from django.contrib import admin

from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.


# Custom user display
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_login', 'is_admin','is_staff','is_provider')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User, AccountAdmin)

