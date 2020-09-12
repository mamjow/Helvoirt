from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Account


# User Serializer
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = Account(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'passwords must match.'})
        user.set_password(password)
        user.save()

        return user
