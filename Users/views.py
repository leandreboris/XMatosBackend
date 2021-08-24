from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

from .serializers import UserSerializer, UserRegisterSerializer, LoginSerializer, ProviderRegisterSerializer
from XMatosbackend  import utils

from django.contrib.gis.geoip2 import GeoIP2
from Analytics.signals import object_viewed_signal
from django.core.mail import EmailMessage
from Codes.models import Code




# Registration APIs

class UserRegistrationAPI(generics.GenericAPIView):


    serializer_class = UserRegisterSerializer
    
    def post(self, request, *args, **kwargs):

        # Saving data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        

        # Tracking the ip address
        ip = utils.get_client_ip(request)

        # Saving the last_ip and setting activity to False
        user.last_ip = ip
        user.is_active = False

        # Generate the code
        code = Code.objects.create(user=user)

        # Fetch the email
        usermail = user.email

        # Email sending
        email = EmailMessage(
            'Activate your account',
            'Hi  ' + str(code.user)+ "!" + "\nPlease activate your account with " + str(code.number), 
            '',
            [usermail],
         
         )
        email.send(fail_silently=False)

        user.save()
       
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



class ProviderRegistrationAPI(generics.GenericAPIView):


    serializer_class = ProviderRegisterSerializer
    
    def post(self, request, *args, **kwargs):
      
       # Saving data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Tracking the ip address
        ip = utils.get_client_ip(request)

        # Saving the last_ip and setting activity to False
        user.last_ip = ip
        user.is_active = False

        # Generate the code
        code = Code.objects.create(user=user)

        # Fetch the email
        usermail = user.email

        # Email sending
        email = EmailMessage(
            'Activate your account',
            'Hi  ' + str(code.user)+ "!" + "\nPlease activate your account with " + str(code.number), 
            '', 
            [usermail],
         
         )
        email.send(fail_silently=False)

        user.save()
       
        # Using geoip2 to get the location
        g = GeoIP2()
        location = g.city("41.77.119.167") # Production, normally tracked IP
        location_country = location["country_name"]




        # We check whether the IP is local or not
        if location_country != "Morocco":
          # Another API for the code verification
          print(location_country)
        

        

        context = {
            "IP address": ip,
            "Localization" : location,
        }


        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : AuthToken.objects.create(user)[1],
            "analytics" : context,
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
    # object_viewed_signal.send(self.request.user.__class__, instanceID=self.request.user.id, request=self.request)
    return self.request.user
  
