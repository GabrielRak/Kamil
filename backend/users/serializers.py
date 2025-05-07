from rest_framework import serializers
from .models import CustomUser
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio']

@require_http_methods(['POST'])
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=False)  
    password2 = serializers.CharField(write_only=False)

    ...

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    
@require_http_methods(['POST'])
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user