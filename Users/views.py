from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

from .serializers import UserSerializer, UserRegisterSerializer


from django.contrib.gis.geoip2 import GeoIP2


# Registration API

class RegistrationAPI(generics.GenericAPIView):


    serializer_class = UserRegisterSerializer
    
    def post(self, request, *args, **kwargs):

        # Tracking the ip address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        g = GeoIP2()
        location = g.city(ip)
        location_country = location["country_name"]
        context = {
            "location_country": location_country,
        }

        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "context" : context,
            "token" : AuthToken.objects.create(user)[1]
        })
