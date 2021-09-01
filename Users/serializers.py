from XMatosbackend.utils import get_client_ip
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
import django.contrib.auth.password_validation as validators





# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validators.validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.last_ip = get_client_ip(self.context['request'])
        instance.save()

        return instance



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'telephone','adresse', 'avatar',)
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        
        if validated_data['first_name'] != '':
            instance.first_name = validated_data['first_name']
        if validated_data['last_name'] != '':  
            instance.last_name = validated_data['last_name']
        if validated_data['email'] != '':
            instance.email = validated_data['email']
        if validated_data['username'] != '':
            instance.username = validated_data['username']
        if validated_data['telephone'] != '':
            instance.telephone = validated_data['telephone']
        if validated_data['avatar'] != '':
            instance.avatar = validated_data['avatar']
        if validated_data['adresse'] != '':
            instance.avatar = validated_data['adresse']
        
        instance.last_ip = get_client_ip(self.context['request'])
        instance.save()
        return instance
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

    

