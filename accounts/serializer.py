from rest_framework import serializers
from accounts.models import Account
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password')

    def validate(self, data):
        user = Account(**data)
        password = data.get('password')
        try:
            validate_password(user=user, password=password)
        except ValidationError as err:
            serializer_err = serializers.as_serializer_error(err)
            raise ValidationError(
                {'password': serializer_err['non_field_errors']}
            )

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', "is_customer", "is_vendor")