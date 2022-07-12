from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers

class CreateAccount(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, valid_data):
        user_id = valid_data['username']
        pwd = valid_data['password']
        user = User.objects.create(
            username=user_id,
            password=pwd
        )
        user.set_password(pwd)
        user.save()
        return user

class LoginAccount(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')