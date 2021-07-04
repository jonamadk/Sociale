from .models import UserModel
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSignupSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(validators=[UniqueValidator(
        UserModel.objects.all())], max_length=None, required=True)
    password = serializers.CharField(
        min_length=8, max_length=None, write_only=True)

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'phonenumber',
                  'first_name', 'last_name', 'id']


class UserSigninSerizalizer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['email', 'password']


class UserUpdateSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(validators=[UniqueValidator(
        UserModel.objects.all())], max_length=None, required=True)

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'phonenumber',
                  'first_name', 'last_name', 'id']


class UserPasswordUpdateSerializer(serializers.ModelSerializer):

    new_password = serializers.CharField(
        min_length=8, max_length=None, write_only=True)

    class Meta:
        model = UserModel
        fields = ['new_password']


class UserPasswordResetSerializaer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ["email"]


class OTPSendMailSerializaer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ["email", ]


class OTPVerificationSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserModel
        fields = ["email", "otp_code"]


class UserGroupSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserModel
        fields = ["groups"]


class MultiFactorAuthenticationSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserModel
        fields = ["email_two_factor_auth", "totp_two_factor_auth",
                  "email_and_sms_two_factor_auth"]


class DisableMultiFactorSerializer(serializers.ModelSerializer):

    status = serializers.BooleanField(default=False)

    class Meta:

        model = UserModel
        fields = ["status"]


class GetPhoneNumberFromEmailSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserModel
        fields = ["phonenumber"]
