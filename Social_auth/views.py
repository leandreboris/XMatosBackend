from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import GoogleSocialAuthSerializer, FacebookSocialAuthSerializer



# Create your views here.

# Google Social authentifications view

class GoogleSocialAuth(generics.GenericAPIView):
  serializer_class = GoogleSocialAuthSerializer

  
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    data = ((serializer.validated_data['auth_token']))
    return Response(data)



# Facebook Social authentifications view

class FacebookSocialAuth(generics.GenericAPIView):
  serializer_class = FacebookSocialAuthSerializer

  
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    data = ((serializer.validated_data['auth_token']))
    return Response(data)



