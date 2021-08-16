from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

from .serializers import UserSerializer, UserRegisterSerializer, LoginSerializer, ProviderRegisterSerializer


from django.contrib.gis.geoip2 import GeoIP2


# Registration APIs

class UserRegistrationAPI(generics.GenericAPIView):


    serializer_class = UserRegisterSerializer
    
    def post(self, request, *args, **kwargs):

        # # Tracking the ip address
        # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(',')[0]
        # else:
        #     ip = request.META.get('REMOTE_ADDR')


        # # Using geoip2 to get the location
        # g = GeoIP2()
        # location = g.city(ip)
        # location_country = location["country_name"]
        # context = {
        #     "location_country": location_country,
        # }

        # Saving data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : AuthToken.objects.create(user)[1]
        })



class ProviderRegistrationAPI(generics.GenericAPIView):


    serializer_class = ProviderRegisterSerializer
    
    def post(self, request, *args, **kwargs):
        # Saving data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()


        # Tracking the ip address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Using geoip2 to get the location
        g = GeoIP2()
        location = g.city("41.77.119.167")
        location_country = location["country_name"]
        if location_country != "Morocco":
          print(location_country)

        context = {
            "IP address": ip,
        }


        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : AuthToken.objects.create(user)[1],
            "context" : context,
        })





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Login API
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data
    _, token = AuthToken.objects.create(user)
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })


# Retrieve user API
# Get User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user