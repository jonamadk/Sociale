from qrotp.views import TOTPVerifyView
from django.shortcuts import render
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from django.http import request, HttpResponse
from .serializers import *
from .models import UserModel
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from django.core.mail import send_mail
from .otp_generator import *
from decouple import config
from .utils import send_sms
from qrotp.models import MFHash
import pyotp
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from group.permissions import has_permission


class UserSignupView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('user.add_usermodel')
    def post(self, request, *args, **kwargs):
        ''' 
        POST Method for the new user registeration

        Checks if the incoming request data are validated and
        creates the user.

        '''

        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            password = data.get('password')
            confirm_password = request.data.get('confirm_password')

            if password == confirm_password:
                user = UserModel.objects.create(email=data.get('email'),
                                                username=data.get('username'),
                                                phonenumber=data.get(
                                                    'phonenumber'),
                                                password=make_password(
                                                    data.get('password')),
                                                first_name=data.get(
                                                    'first_name'),
                                                last_name=data.get('last_name')


                                                )
                token = Token.objects.create(user=user)
                mfa_hash = MFHash.objects.create(user=user)

                try:
                    groups = request.data.get('groups')

                    for items in groups:

                        group_obj = Group.objects.get(id=items)

                        user.groups.add(group_obj)

                    return Response({"key": get_object_or_404(Token, user=user).key, "user": user.username},
                                    status=status.HTTP_200_OK)

                except Exception as e:
                    return Response({"status": "User created but permission group is not added"}, status=status.HTTP_501_NOT_IMPLEMENTED)

            return Response({"status": "Password didn't match"}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):

    ''' 
        GET Method for viewing the user's  list.
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, DjangoModelPermissions]
    queryset = UserModel.objects.all()
    serializer_class = UserSignupSerializer


class UserUpdateView(generics.UpdateAPIView):

    ''' 
        PUT Method for updating the User's data.
        Does not take the password field.
    '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserModel.objects.all()
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return UserModel.objects.get(username=self.request.user.username)


class UserProfilePasswordUpdateView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        ''' 
        PUT Method for user password update.

        Checks the old password
            if True:
                  Allows to update the new password.SSSS
        '''

        serializer = UserPasswordUpdateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = UserModel.objects.get(id=request.user.id)
            oldpassowrd = request.data.get("old_password")
            newpassword = data.get("new_password")
            if not user.check_password(oldpassowrd):
                return Response({"old_password": ["Old Password didn't match"]}, status=status.HTTP_403_FORBIDDEN)
            user.password = make_password(newpassword)
            user.save()

            return Response({"status": "password changed successfully", "user": user.username}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):

    ''' 
        DELETE Method for destroying the user.
    '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, DjangoModelPermissions]

    def delete(self, request, *args, **kwargs):

        user = UserModel.objects.get(id=request.data.get("id"))
        user.delete()

        return Response({"success": True}, status=status.HTTP_200_OK)


class UserRetrieveView(generics.RetrieveAPIView):

    '''  
        GET Method for viewing the user list.

    '''

    authentication_classes = [TokenAuthentication]
    permission_classed = [IsAuthenticated]

    queryset = UserModel.objects.all()
    serializer_class = UserSignupSerializer

    def get_object(self):
        return UserModel.objects.get(username=self.request.user.username)


class UserSiginView(APIView):

    authencation_class = [TokenAuthentication]
    permission_class = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ''' 
        POST Method for the user logging activity

        Authenticate User with Email and password


        '''

        serializer = UserSigninSerizalizer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                user = UserModel.objects.get(email=data.get("email"))

            except:
                return Response({"status": "no user with such credentials"}, status=status.HTTP_403_FORBIDDEN)
            user = authenticate(username=user.username,
                                password=data.get('password'))

            if user is not None:
                user.otp_code = otp_code_generator()
                otp_code = user.otp_code
                user.save()
                return Response({"key": get_object_or_404(Token, user=user).key, "user": user.username},
                                status=status.HTTP_200_OK)
            else:
                return Response({"status": "no user with such credentials"}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TwoFactorCheckandRoute(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ''' 
        Checks if the authentication method 
        is associated with email based or
        sms based 

        '''

        user = UserModel.objects.get(id=request.user.id)

        if user.email_and_sms_two_factor_auth == True:
            phonenumber = user.phonenumber
            otp_code = user.otp_code
            send_sms(otp_code, phonenumber)

            return Response({"Status": " SMS Based", "user": user.username},
                            status=status.HTTP_200_OK)

        elif user.email_two_factor_auth == True:
            if user is not None:
                user.otp_code = otp_code_generator()
                otp_code = user.otp_code
                user.save()

            email_plaintext_message = " Your OTP code is : {} . Dear {}, Please Enter the code for verification ".format(
                user.otp_code, user.username)
            send_mail(
                # title:
                "OTP Verification for  {title}".format(title="SocialIE"),
                # message:
                email_plaintext_message,
                # from:
                config('EMAIL_HOST_USER'),

                # to:
                [user.email]

            )
            return Response({"status": "Email Based"}, status=status.HTTP_200_OK)

        elif user.totp_two_factor_auth == True:

            return Response({'message': 'Totp Implemented'}, status=status.HTTP_200_OK)

        else:
            return Response({"message": "Two Factor Auth not implemented"}, status=status.HTTP_404_NOT_FOUND)


class SendOTPInMailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        POST Method Sending OTP in Email

        '''

        try:

            user = UserModel.objects.get(id=request.user.id)
            if user.email_two_factor_auth == True:

                email_plaintext_message = " Your OTP code is : {} . Dear {}, Please Enter the code for verification ".format(
                    user.otp_code, user.username)
                send_mail(
                    # title:
                    "OTP Verification for  {title}".format(title="SocialIE"),
                    # message:
                    email_plaintext_message,
                    # from:
                    config('EMAIL_HOST_USER'),

                    # to:
                    [user.email]

                )

                return Response({"status": "Email Send"}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "Email based 2f not enabled"}, status=status.HTTP_501_NOT_IMPLEMENTED)

        except Exception as e:

            return Response({"message": "Email is not associated to account"}, status=status.HTTP_400_BAD_REQUEST)


class ForgetPasswordView(APIView):

    def post(self, request, *args, **kwargs):
        '''
        POST Method for adding new password

        routed from forgot password

        '''

        serializer = UserPasswordResetSerializaer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            email = data.get('email')

            try:
                user = UserModel.objects.get(email=email)
                user.otp_code = otp_code_generator()
                user.save()
                email_plaintext_message = " Your OTP code is : {} . Dear {}, Please Enter the code for verification ".format(
                    user.otp_code, user.username)
                send_mail(
                    # title:
                    "OTP Verification for  {title}".format(title="SocialIE"),
                    # message:
                    email_plaintext_message,
                    # from:
                    config('EMAIL_HOST_USER'),

                    # to:
                    [user.email]

                )

                return Response({"status": "OTP has been send"}, status=status.HTTP_200_OK)

            except Exception as e:

                return Response({"message": "Sorry this email is not associated to account"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OTPVerifyForForgetPassword(APIView):

    '''

    OTP verification.

    Thus Send OTP in user's mail is matched with the associated
    user's db current OTP code for tasks like , login & forgot password.

    '''

    def post(self, request, *args, **kwargs):

        seralizer = OTPVerificationSerializer(data=request.data)
        if seralizer.is_valid():
            data = seralizer.validated_data
            user = UserModel.objects.get(email=data.get("email"))
            otp_code = user.otp_code
            if otp_code == data.get("otp_code"):

                return Response({"status": "OTP Verified"},
                                status=status.HTTP_200_OK)
            else:
                return Response({"status": "Incorrect OTP"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddNewPassword(APIView):

    def post(self, request, *args, **kwargs):

        new_password = request.data.get("new_password")
        confirm_password = request.data.get("confirm_password")

        if new_password == confirm_password:
            user = UserModel.objects.get(email=request.data.get("email"))
            user.password = make_password(new_password)
            user.save()

            return Response({"status": True, "msg": "Password updated !!"}, status=status.HTTP_200_OK)

        else:

            return Response({"status": False, "msg": "Password confirmation not matched !!"}, status=status.HTTP_400_BAD_REQUEST)


class OTPVerifyView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''

        OTP verification.

        Thus Send OTP in user's mail is matched with the associated
        user's db current OTP code for tasks like , login & forgot password.

        '''

        seralizer = OTPVerificationSerializer(data=request.data)
        if seralizer.is_valid():
            data = seralizer.validated_data
            user = UserModel.objects.get(id=request.user.id)
            otp_code = user.otp_code
            if otp_code == data.get("otp_code"):
                return Response({"status": "OTP Verified"},
                                status=status.HTTP_200_OK)
            else:
                return Response({"status": "Incorrect OTP"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SelectTwoFactorAuthView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        POST Method to enable the Email based 
        two factor authentication

        returns the 2f service status for that user
        '''
        serializer = MultiFactorAuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            email = data.get("email_two_factor_auth")
            totp = data.get("totp_two_factor_auth")
            email_and_sms = data.get("email_and_sms_two_factor_auth")
            try:
                user = UserModel.objects.get(id=request.user.id)
                if email == True:
                    user.email_two_factor_auth = True
                    user.totp_two_factor_auth = False
                    user.email_and_sms_two_factor_auth = False
                    user.save()
                    return Response({"msg": "Enabled email based auth", "Email auth status": user.email_two_factor_auth}, status=status.HTTP_200_OK)

                elif totp == True:
                    user.email_two_factor_auth = False
                    user.totp_two_factor_auth = True
                    user.email_and_sms_two_factor_auth = False
                    user.save()
                    return Response({"msg": "Enabled totp based auth", "Totp auth status": user.totp_two_factor_auth}, status=status.HTTP_200_OK)

                else:
                    user.email_two_factor_auth = False
                    user.totp_two_factor_auth = False
                    user.email_and_sms_two_factor_auth = True
                    user.save()
                    return Response({"msg": "Enabled SMS based auth", "Email and Sms auth status": user.email_and_sms_two_factor_auth}, status=status.HTTP_200_OK)

            except:
                return Response({"msg": "Couldn't enable the Email based 2f"}, status=status.HTTP_501_NOT_IMPLEMENTED)


class DisableTwoFactorAuthView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        POST Method to disable the Email based 
        two factor authentication

        returns the 2f service status for that user
        '''
        serializer = DisableMultiFactorSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            try:

                if data.get("status") == False:
                    user = UserModel.objects.get(id=request.user.id)
                    user.totp_two_factor_auth = False
                    user.email_two_factor_auth = False
                    user.email_and_sms_two_factor_auth = False
                    user.save()

                    return Response({"Email based 2f auth status": user.email_two_factor_auth, "Totp based 2f auth status": user.totp_two_factor_auth, "Email and sms based 2f": user.email_and_sms_two_factor_auth}, status=status.HTTP_200_OK)

            except:
                return Response({"msg": "Couldnt Disable the Email based 2f"}, status=status.HTTP_501_NOT_IMPLEMENTED)


class UserAuthStatusView(generics.RetrieveAPIView):

    '''  
        GET Method for viewing the user list.

    '''

    authentication_classes = [TokenAuthentication]
    permission_classed = [IsAuthenticated]

    queryset = UserModel.objects.all()
    serializer_class = MultiFactorAuthenticationSerializer

    def get_object(self):
        return UserModel.objects.get(username=self.request.user.username)


class GetPhoneNumberFromEmailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        user = UserModel.objects.get(id=request.user.id)
        serializer = GetPhoneNumberFromEmailSerializer(user)

        return Response({"status": serializer.data})


class OTPSendInUserEmail(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        POST Method Sending OTP in Email

        '''

        try:

            user = UserModel.objects.get(id=request.user.id)

            email_plaintext_message = " Your OTP code is : {} . Dear {}, Please Enter the code for verification ".format(
                user.otp_code, user.username)
            send_mail(
                # title:
                "OTP Verification for  {title}".format(title="SocialIE"),
                # message:
                email_plaintext_message,
                # from:
                config('EMAIL_HOST_USER'),

                # to:
                [user.email]

            )

            return Response({"status": "Email Send"}, status=status.HTTP_200_OK)

        except Exception as e:

            return Response({"message": "Email is not associated to account"}, status=status.HTTP_400_BAD_REQUEST)


class CheckUserState(APIView):

    '''
    Checks the local storage token with the request token 
    and the username

    Returns permissions of that user 

    '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        token_is = request.data.get("token")
        username_is = request.data.get("username")

        try:
            token = Token.objects.get(key=token_is)
            key = token.key
            user = token.user
        except:
            return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)
        token_verification = False
        if token_is == str(key) and username_is == str(user):

            user_is = UserModel.objects.get(id=user.id)
            try:
                user_group = user_is.groups.all()
                permission_list = []
                for group in user_group:
                    group_is = Group.objects.get(id=group.id)
                    permissions_are = group_is.permissions.all()
                for permission in permissions_are:
                    permission_list.append(permission.codename)

                return Response({"success": True, "permissions": permission_list}, status=status.HTTP_200_OK)
            except:

                user_permissions = user_is.user_permissions.all()
                permission_list = []
                for permission in user_permissions:
                    permission_list.append(permission.codename)
                return Response({"success": True, "permissions": permission_list}, status=status.HTTP_200_OK)

        else:
            return Response({"suceess": False}, status=status.HTTP_400_BAD_REQUEST)
