from accounts.models import Account
from accounts.serializer import UserCreateSerializer, UserSerializer
from rest_framework import serializers


class VendorCreateSerializer(UserCreateSerializer):
    def create(self, validated_data):
        user = Account.objects.create_vendor(**validated_data)
        return user


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'is_vendor', 'is_active')
