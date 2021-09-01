from django.urls import path, include
from .views import *
from Profile_updates.views import * 



urlpatterns = [


    path('auth', include('knox.urls')),
    path('auth/login', LoginAPI.as_view(), name='login'),
    path('auth/register/user', UserRegistrationAPI.as_view(), name='User Registration'),
    path('auth/register/provider', ProviderRegistrationAPI.as_view(), name='Provider Registration'),
    path('auth/verify-code', VerifyCode.as_view(), name='verify-code'),



    path('user', UserAPI.as_view()),
    path('user/factures', FactureViewSet.as_view({'get': 'retrieve'})),
    path('user/commandes', CommandeViewSet.as_view({'get': 'retrieve'})),
    path('user/articles', ArticleViewSet.as_view({'get': 'retrieve'})),
    path('user/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('user/update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),



]


