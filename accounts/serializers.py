from pyexpat import model
from django.conf import settings
from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import User
from parts import models

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'roles', 'national_code']

    def get_roles(self, obj):
        groups = obj.groups.all()
        return [group.name for group in groups]
    
    def validate_username(self, value):
        # override default username validations
        return value
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