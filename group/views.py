from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from ast import dump
from group.permissions import has_permission
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models.query import QuerySet
from django.http import request, response
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import generics
from django.contrib.auth.models import AnonymousUser, Group
from .serializer import *
from user.views import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser,  DjangoModelPermissions
from django.contrib.auth.models import Permission
from django.core import serializers
from .permissions import has_permission
from django.shortcuts import render
import json


class UsersGroupCreateView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @has_permission('group.add_group')
    def post(self, request, *args, **kwargs):
        '''
        POST Method for Group Creation
        Only System Admin can create Group and
        assign permissions to it.

        '''

        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            group = Group.objects.create(name=data.get('name'))
            try:
                permissions = request.data.get('permissions')
                for permission_index in permissions:
                    permission = Permission.objects.get(id=permission_index)
                    group.permissions.add(permission)
            except Exception as e:
                print("Error in creating")
            return Response({"status": "Group Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserGroupList(generics.ListAPIView):

    '''
    GET Method for Retrieving Group
    Only System Admin can Retrieve Group data

    '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, DjangoModelPermissions]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupUpdateView(APIView):

    '''
        PUT Method for updating the Group & permissions.
        Only System Admin can Update Group data
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @ has_permission('group.change_group')
    def patch(self, request, *args, **kwargs):

        group = Group.objects.get(id=request.data.get('id'))
        group.name = request.data.get("name")
        group.save()
        permissions_are = group.permissions.all()
        for permission in permissions_are:
            group.permissions.remove(permission)

        try:
            permissions = request.data.get('permissions')
            for permission_index in permissions:
                permission = Permission.objects.get(id=permission_index)
                group.permissions.add(permission)

        except Exception as e:
            return Response({"success": False, "msg": "Error in adding new permissions"})

        return Response({"status": True, "msg": "Group and persmisssions sucessfully updated"}, status=status.HTTP_200_OK)


class GroupDeleteView(generics.DestroyAPIView):

    '''
        DELETE Method for Deleting The Group
        Only System Admin can DELETE Group data.

    '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = GroupSerializer

    @ has_permission('group.delete_group')
    def delete(self, request, *args, **kwargs):

        group_id = self.request.data.get("id")
        group = Group.objects.get(id=group_id)
        all_users = UserModel.objects.filter(groups=group)
        default_permission_codename = [
            'view_usermodel', 'change_usermodel', 'view_campaign']
        default_permission_index = []
        for permission_codename in default_permission_codename:

            permission = Permission.objects.get(codename=permission_codename)
            default_permission_index.append(permission.id)
        if not all_users:
            for user in all_users:
                user_is = UserModel.objects.get(id=user.id)
                for permission_index in default_permission_index:
                    user_is.user_permissions.add(permission_index)
            group.delete()
            return Response({"success": True}, status=status.HTTP_200_OK)
        else:
            for user in all_users:
                user_is = UserModel.objects.get(id=user.id)
                for permission_index in default_permission_index:
                    user_is.user_permissions.add(permission_index)
            group.delete()

        return Response({"success": True}, status=status.HTTP_200_OK)


class GetPermissionsList(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class GetUserGroupandPermissions(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]

    def post(self, request, *args, **kwargs):

        try:

            user = UserModel.objects.get(id=request.data.get("user_id"))
            user_group = user.groups.all()
            permission_list = []
            permission_are_list = []
            group_name = []
            for group in user_group:
                group_is = Group.objects.get(id=group.id)
                group_name.append(group_is.name)
                permissions_are = group_is.permissions.all()
                permission_are_list.append(permissions_are)

            for permission_are_item in permission_are_list:
                for permission in permission_are_item:
                    print(permission)

                    permission_list.append(
                        permission.codename)

            permission_list = set(permission_list)
            return Response({"success": True, "group_associated": group_name, "permission_list": permission_list}, status=status.HTTP_200_OK)

        except:

            return Response({"success": False}, status=status.HTTP_501_NOT_IMPLEMENTED)


class AdjustedPermissions(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):

        permission = Permission.objects.all()
        serializer = PermissionSerializer(permission, many=True)

        permission_data = serializer.data
        permissions = permission_data
        list_to_remove = ['_userobjectpermission', '_logentry', '_token',
                          '_groupobjectpermission', '_session', '_mfhash', '_contenttype']
        for permission in permissions[:]:

            for item in list_to_remove:
                if item in permission['codename']:
                    permissions.remove(permission)

        granted_permission = permissions

        return Response({"permissions": granted_permission})


class GetPermissionsFromGroup(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]

    def post(self, request, *args, **kwargs):

        try:

            groups_is = Group.objects.get(id=request.data.get('group_id'))
            print(groups_is)
            permissions_in_group = groups_is.permissions.all()
            permission_list = []

            for permission in permissions_in_group:
                print(permission)
                permission_list.append(
                    permission.codename)

            permission_list = set(permission_list)
            permission_list_is = list(permission_list)
            data = {"group": groups_is.name, "permissons": permission_list_is}
            return Response(data, status=status.HTTP_200_OK)

        except:

            return Response({"success": False}, status=status.HTTP_501_NOT_IMPLEMENTED)


class TestEmail(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        POST Method Sending OTP in Email

        '''

        try:

            user = UserModel.objects.get(id=request.user.id)

            email_plaintext_message = " Test Mail. Dear {}, Please Enter the code for verification ".format(
                user.username)
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


class EditUserGroupAssociationView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        user = UserModel.objects.get(id=request.data.get("id"))
        all_groups = user.groups.all()
        try:
            for group in all_groups:
                user.groups.remove(group.id)
        except:
            return Response({"success": False})

        try:
            add_groups_list = request.data.get("groups")
            for group in add_groups_list:
                user.groups.add(group)

            return Response({"success": True})
        except:

            return Response({"success": False})
