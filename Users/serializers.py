from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate




# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email',)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Register Serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name','last_ip', 'avatar',)
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],validated_data['username'], validated_data['password'], validated_data['first_name'], validated_data['last_name'], validated_data['last_ip'], validated_data['avatar'])
        return user

class ProviderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'cin', 'adresse', 'telephone', 'first_name', 'last_name','last_ip', 'avatar',)
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_provider(validated_data['email'],validated_data['username'], validated_data['password'], validated_data['cin'], validated_data['adresse'], validated_data['telephone'], validated_data['first_name'], validated_data['last_name'], validated_data['last_ip'], validated_data['avatar'])
        return user



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 




# Login Serializer

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

    

