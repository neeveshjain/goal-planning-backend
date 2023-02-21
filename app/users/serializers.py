from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:  
        model = User
        # These are the fields this serializer will return
        fields = ('first_name', 'last_name', 'email', 'password')

    def validate(self, data):
        """
        Validate passwords with some basic built-in Django rules that will encourage users to create stronger passwords
        """
        # Retrieve user and password data from this serializer parameters
        user = User(**data)
        password = data.get('password')

        # Logic to validate password, if password is good return it and continue, else throw an error
        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password': serializer_errors['non_field_errors']}
            )
        
        return data

    def create(self, validated_data):
        """
        Create user via serializer approach
        """
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user
    
# New class used to output our desired fields when serializing
class UserSerializer(serializers.ModelSerializer):
    class Meta:  
        model = User
        fields = ('first_name', 'last_name', 'email')
