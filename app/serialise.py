# from django.db import models
# from django.db.models import fields
from rest_framework import serializers
from app.models import Package, UserRegister,PaymentDetails
# from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegisterSerialiser(serializers.ModelSerializer):
    class Meta:
        model=UserRegister
        exclude=['last_login','is_superuser','is_staff','is_active','date_joined']
        # fields=['uid','name','gender','father_name','mother_name',
        # 'mobile_number','email_id','education','dob','profile_created_by']

class LoginSerializer(serializers.Serializer):
    mobile_number = serializers.CharField()
    password = serializers.CharField()

class PaymentDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        models=PaymentDetails
        fields='__all__'

class PackageSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields=['amount','membership']

# class PersonalDetailsSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model=PersonalDetails
#         fields="__all__"

# class UserSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password','email']