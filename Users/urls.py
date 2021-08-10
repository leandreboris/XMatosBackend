from django.urls import path, include
from .views import RegistrationAPI
from knox import  views as knox_views

urlpatterns = [
    path('auth', include('knox.urls')),
    path('auth/register', RegistrationAPI.as_view()),
]
