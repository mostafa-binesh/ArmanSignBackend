from pyexpat import model
from urllib.parse import parse_qsl
from django.conf import settings
from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import User

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'roles', 'national_code']


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        # Add user to Operator group
        operator_group, created = Group.objects.get_or_create(name='Operator')
        user.groups.add(operator_group)

        # Generate the password from the national_code field
        national_code = validated_data.get('national_code')
        user.set_password(national_code)

        # Save the user instance to the database
        user.save()

        return user

    def get_roles(self, obj):
        groups = obj.groups.all()
        return [group.name for group in groups]
    
    # def validate_username(self, value):
    #     # override default username validations
    #     return value
    def validate_username(self, value):
        # Custom validation for username
        # raise serializers.ValidationError("نام کاربری نمی تواند خالی باشد.")
        # if not value:  # Check if the username is not empty
            # raise serializers.ValidationError("نام کاربری نمی تواند خالی باشد.")
        # Add any other custom validations here if needed
        return value
    # username_validator = UnicodeUsernameValidator()
class UserGroupSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'national_code']

    def get_role(self, obj):
        return 'operator';
    
    def validate_username(self, value):
        # override default username validations
        return value

class OperatorFilterSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'title', 'national_code']
        
    def get_title(self, obj):
        return f"{obj.first_name} {obj.last_name}"