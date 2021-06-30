import pyotp
from rest_framework import serializers
from .models import MFHash
import pyotp
from user.models import UserModel


class UserSigninTOTPSerizalizer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['otp_code', ]
