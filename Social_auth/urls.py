from django.urls import path
from .views import GoogleSocialAuth, FacebookSocialAuth



urlpatterns = [
    path('social_auth/google', GoogleSocialAuth.as_view(), name='google_login'),
    path('social_auth/facebook', FacebookSocialAuth.as_view(), name = 'facebook_login'),

]