from pyexpat import model
from urllib.parse import parse_qsl
from django.conf import settings
from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


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


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
