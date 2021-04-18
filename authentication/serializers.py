from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    password=serializers.CharField(min_length=6,max_length=64,write_only=True)
    email=serializers.EmailField(min_length=6,max_length=64)
    first_name=serializers.CharField(min_length=2,max_length=64)
    last_name=serializers.CharField(min_length=2,max_length=64)
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
    
    def validate(self, data):
        email=data.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'info':('email already exits!')})
        return super().validate(data)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializers(serializers.ModelSerializer):
    password=serializers.CharField(min_length=6,max_length=64,write_only=True)
    username=serializers.CharField(min_length=2,max_length=64)
    class Meta:
        model=User
        fields=[
            'username',
            'password'
        ]




