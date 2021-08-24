from django.urls import path, include
from .views import UserRegistrationAPI, LoginAPI, ProviderRegistrationAPI, UserAPI

urlpatterns = [
    path('auth', include('knox.urls')),
    path('user', UserAPI.as_view()),

    path('auth/login', LoginAPI.as_view()),
    path('auth/register/user', UserRegistrationAPI.as_view(), name='User Registration'),
    path('auth/register/provider', ProviderRegistrationAPI.as_view(), name='Provider Registration'),
   

]


