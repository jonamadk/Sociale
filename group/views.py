from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models.query import QuerySet
from django.http import request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import generics
from django.contrib.auth.models import Group
from .serializer import *
from user.views import *
from rest_framework.permissions import IsAuthenticated , IsAdminUser,  DjangoModelPermissions
from django.contrib.auth.models import Permission
from django.core import serializers


class UsersGroupCreateView(APIView):


    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def post(self , request , *args, **kwargs):

        '''
        POST Method for Group Creation
        Only System Admin can create Group and 
        assign permissions to it.

        '''

        serializer = GroupSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            group = Group.objects.create(name = data.get('name'))
            try:
                permissions = request.data.get('permissions')
                for permission_index in permissions:
                    permission=Permission.objects.get(id=permission_index)
                    group.permissions.add(permission)
            except Exception as e:
                print("Error in creating")
            return Response({"status":"Group Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
class GetUserGroupList(generics.ListAPIView):

  
    '''
    GET Method for Retrieving Group
    Only System Admin can Retrieve Group data

    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, DjangoModelPermissions]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    



class GroupUpdateView(generics.UpdateAPIView):

    ''' 
        PUT Method for updating the Group & permissions.
        Only System Admin can Update Group data
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, DjangoModelPermissions]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class GroupDeleteView(generics.DestroyAPIView):

    ''' 
        DELETE Method for Deleting The Group
        Only System Admin can DELETE Group data.
        
    '''
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, DjangoModelPermissions]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer





class GetPermissionsList(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, DjangoModelPermissions]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer




