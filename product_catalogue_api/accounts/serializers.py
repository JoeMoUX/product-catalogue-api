from rest_framework import serializers
from .models import UserAccount
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'email', 'password']
        
    def validate(self, attrs):
        email = attrs.get('email',)
        first_name = attrs.get('first_name',)
        last_name = attrs.get('last_name',)
        
        if not first_name.isalpha():
            raise serializers.ValidationError('The first name should be only be alphabets')
        if not last_name.isalpha():
            raise serializers.ValidationError('The last name should be only be alphabets')
        
        return attrs
    
    def create(self, validated_data):
        return UserAccount.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    first_name = serializers.CharField(
        max_length=68, min_length=2, read_only=True)
    last_name = serializers.CharField(
        max_length=68, min_length=2, read_only=True)
    tokens = serializers.CharField(
        max_length=100, min_length=2, read_only=True)
    
    class Meta:
        model = UserAccount
        fields = '__all__'
    
    def validate(self, attrs):
        email = attrs.get('email',)
        password = attrs.get('password',)
        
        user = auth.authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        
        return {
            'email': user.email,
            'tokens': user.tokens,
        }
        

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']
        
        
class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = UserAccount.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return user
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        