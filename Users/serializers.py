from XMatosbackend.utils import get_client_ip
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate





# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Register Serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name','avatar',)
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],validated_data['username'], validated_data['password'], validated_data['first_name'], validated_data['last_name'], validated_data['avatar'])
        user.last_ip = get_client_ip(self.context['request'])
        user.save()
        return user

class ProviderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'cin', 'adresse', 'telephone', 'first_name', 'last_name','avatar',)
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_provider(validated_data['email'],validated_data['username'], validated_data['password'], validated_data['cin'], validated_data['adresse'], validated_data['telephone'], validated_data['first_name'], validated_data['last_name'],validated_data['avatar'])
        user.last_ip = get_client_ip(self.context['request'])
        user.save()
        return user



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 




# Login Serializer

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_verified:
            user.last_ip = get_client_ip(self.context['request'])
            user.save()
            return user
        raise serializers.ValidationError("Incorrect Credentials")

    

