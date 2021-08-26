from Analytics.models import ArticlesViewed
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import viewsets


from knox.models import AuthToken

from .serializers import *
from XMatosbackend  import utils

from django.contrib.gis.geoip2 import GeoIP2
from Analytics.signals import object_viewed_signal
from django.core.mail import EmailMessage
from Codes.models import Code

from Entities.serializers import FactureSerializer, CommandeSerializer, ArticleSerializer
from Codes.serializers import CodeSerializer
from Entities.models import Commande, Facture, Article
from .models import User


from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

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

        # Fetch the email and generate the token
        usermail = user.email
        token = AuthToken.objects.create(user)[1]

        # URL generation
        current_site = get_current_site(request).domain
        absolute_link='http://' + current_site + reverse('verify-code') + '?id=' + str(code.id)


        # Email sending
        email = EmailMessage(
            'Activate your account',
            'Hi  ' + str(code.user)+ "!" + "\nPlease activate your account with " + str(code.number) +' on this URL ' + absolute_link, 
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
            "token" : token,
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

        # Fetch the email and generate the token
        usermail = user.email
        token = AuthToken.objects.create(user)[1]

        # URL generation
        current_site = get_current_site(request).domain
        absolute_link='http://' + current_site + reverse('verify-code') + '?id=' + str(code.id)


        # Email sending
        email = EmailMessage(
            'Activate your account',
            'Hi  ' + str(code.user)+ "!" + "\nPlease activate your account with " + str(code.number) +' on this URL ' + absolute_link, 
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

# Code verification 
class VerifyCode(generics.GenericAPIView):

  serializer_class = CodeSerializer


  def post(self, request):

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try: 
      id=request.GET.get('id')
      code = Code.objects.get(id=id)
      user = User.objects.get(username=code.user)
      user.is_active=True
      user.save()
      return Response({"Email successfully activated. Please sign up to your account dear " + user.username})
    except :
      return Response({"Error"})




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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Retrieve user API
# Get User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


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

# Get user factures API
class FactureViewSet(viewsets.ViewSet):
    permission_classes = [
    permissions.IsAuthenticated,
      ]
    def retrieve(self, request):
        owner = User.objects.get(id=self.request.user.id)
        queryset = Facture.objects.filter(owner=owner)
        serializer = FactureSerializer(queryset, many=True)
        return Response(serializer.data)

# Get user commandes API
class CommandeViewSet(viewsets.ViewSet):
    permission_classes = [
    permissions.IsAuthenticated,
      ]
    def retrieve(self, request):
        owner = User.objects.get(id=self.request.user.id)
        queryset = Commande.objects.filter(owner=owner)
        serializer = CommandeSerializer(queryset, many=True)
        return Response(serializer.data)

# Get user articles API
class ArticleViewSet(viewsets.ViewSet):
    permission_classes = [
    permissions.IsAuthenticated,
      ]
    def retrieve(self, request):
        provider = User.objects.get(id=self.request.user.id)
        queryset = Article.objects.filter(provider=provider)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)
