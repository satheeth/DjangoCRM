from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Record

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
    
class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ("id", "first_name", "last_name", "email", "phone", "address", "city", "state", "pincode")

