from django.shortcuts import render
from Users.models import User 
from rest_framework import generics, permissions
from .serializers import UpdateUserSerializer, ChangePasswordSerializer



# Change user password API
class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
  
# Update user profile API
class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateUserSerializer
