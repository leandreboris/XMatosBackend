from django.urls import path
from .views import GoogleSocialAuth



urlpatterns = [
    path('social_auth/google', GoogleSocialAuth.as_view(), name='google_login'),
]