from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email')



# Register Serializer

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password',)
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],validated_data['username'], validated_data['password'])
        return user



# Login Serializer
