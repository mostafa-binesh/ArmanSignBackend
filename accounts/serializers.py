from pyexpat import model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.models import User

from parts import models

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']

    def get_role(self, obj):
        return 'operator';

class OperatorFilterSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'title']
        
    def get_title(self, obj):
        return f"{obj.first_name} {obj.last_name}"