import uuid
from django.shortcuts import render
from .serializers import UserSigninTOTPSerizalizer
from .models import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import UserModel
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.contrib.auth import authenticate
import time
import pyotp


class EnableQRBasedTOTP(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        POST Method for adding totp to devices
        returns the QR code URL for scanning.

        '''

        try:
            user = UserModel.objects.get(id=request.user.id)
            mfa_hash = MFHash.objects.get(user=user)
            mfa_hash.mfa_hash = pyotp.random_base32()
            mfa_hash.save()
            uri = pyotp.totp.TOTP(mfa_hash.mfa_hash).provisioning_uri(
                user.email, issuer_name="SocialIE")
            

            # qrcode_uri = "https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl={}".format(
            #     uri)

            return Response({"status": "QR Created", 'qrcode': uri}, status=status.HTTP_201_CREATED)

        except:
            return Response({"status": "QR couldn't be created"}, status=status.HTTP_501_NOT_IMPLEMENTED)


class TOTPVerifyView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        POST Method to to sigin in and
        validate the totp associated with
        device

        '''

        serializer = UserSigninTOTPSerizalizer(data=request.data)
        if serializer.is_valid():

            data = serializer.validated_data
            user = UserModel.objects.get(id=request.user.id)

            if user:

                user = MFHash.objects.get(user=user)

                totp = pyotp.TOTP(user.mfa_hash)
                time.sleep(3)
                otp_code = data.get('otp_code')
                totp = totp.now()
                if totp == otp_code:
                    return Response({'message': 'OTP Verified'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Invalid OTP'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({"Message": "No user with such credentilas"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
