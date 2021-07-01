from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import *
from user.models import UserModel
from .serializers import *
import datetime
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
import pyotp
from template.models import TemplateResource
from group.permissions import has_permission


class TemplateUpload(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        '''
        POST Method for uploading the template

        '''

        serializer = UploadSerializer(data=request.data)
        if request.user.is_authenticated:
            user = UserModel.objects.get(id=request.user.id)
            if serializer.is_valid():
                data = serializer.validated_data
                template = Template.objects.create(name=data.get("name"),
                                                   template_file=data.get(
                                                       'template_file'),
                                                   user=user, created_date=datetime.date.today())

                return Response({"status": True, }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"Messagae": "Not Authenticated"}, status=status.HTTP_401_UNAUTHORIZED)


class TemplateRetrieveView(generics.ListAPIView):

    '''  
        GET Method for viewing the templates.

    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Template.objects.all()
    serializer_class = GetTemplateSerializer

    def get_object(self):
        user = self.request.user
        return Template.objects.filter(user=user)


class TemplateDeleteView(generics.DestroyAPIView):

    ''' 
        DELETE Method for destroying the Template.
    '''

    parser_classes = [MultiPartParser, FormParser]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Template.objects.all()
    serializer_class = UploadSerializer


class TemplateUpdateView(generics.UpdateAPIView):

    '''
        PUT Method for template Update
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Template.objects.all()
    serializer_class = UploadSerializer


class CreateResourceView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('template.add_templateresource')
    def post(self, request, *args, **kwargs):
        '''
        POST Method to create 
        initial template resources

        '''

        serializer = TemplateResourceUpdateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = UserModel.objects.get(id=request.user.id)

            resource = TemplateResource.objects.create(headerBackgroundColor=data.get("headerBackgroundColor"),
                                                       headerFontColor=data.get(
                                                           "headerFontColor"),
                                                       bodyBackgroundcolor=data.get(
                                                           "bodyBackgroundcolor"),
                                                       bodyFontColor=data.get(
                                                           "bodyFontColor"),
                                                       headerNav1=data.get(
                                                           "headerNav1"),
                                                       headerNav2=data.get(
                                                           "headerNav2"),
                                                       headerNav3=data.get(
                                                           "headerNav3"),
                                                       bodyButtonColor=data.get(
                                                           "bodyButtonColor"),
                                                       template_name=data.get(
                                                           "template_name"),
                                                       template_url=data.get(
                                                           "template_url"),
                                                       user=user)

            return Response({"status": True, "id": resource.id, "url": resource.template_url}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateTemplateResourceView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('template.change_templateresource')
    def put(self, request, *args, **kwargs):
        '''

        Update method for updating 
        the associated template resources.

        '''

        serializer = TemplateResourceUpdateSerializer(data=request.data)
        user = UserModel.objects.get(id=request.user.id)
        if serializer.is_valid():
            data = serializer.validated_data
            try:

                resource = TemplateResource.objects.get(
                    id=request.data.get('template_resource_id'))
                resource.headerBackgroundColor = data.get(
                    "headerBackgroundColor")
                resource.headerFontColor = data.get("headerFontColor")
                resource.bodyBackgroundcolor = data.get("bodyBackgroundcolor")
                resource.bodyFontColor = data.get("bodyFontColor")
                resource.headerNav1 = data.get("headerNav1")
                resource.headerNav2 = data.get("headerNav2")
                resource.headerNav3 = data.get("headerNav3")
                resource.bodyButtonColor = data.get("bodyButtonColor")

                resource.user = user

                resource.template_name = data.get("template_name")

                resource.save()

                return Response({"status": True}, status=status.HTTP_200_OK)
            except:
                return Response({"status": False}, status=status.HTTP_501_NOT_IMPLEMENTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TemplateResourceListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @has_permission('template.view_templateresource')
    def get(self, request, *args, **kwargs):
        '''
        GET Method 
        Returns the template resources 
        '''

        try:
            user = UserModel.objects.get(id=request.user.id)
            resources = TemplateResource.objects.filter(user=user)
            serializer = TemplateResourceSerializer(resources, many=True)

            return Response({'status': True, "data": serializer.data}, status=status.HTTP_200_OK)

        except:

            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND)


class TemplateResourceRetrieveView(APIView):

    parser_classes = [MultiPartParser, FormParser]

    @has_permission("template.view_templateresource")
    def get(self, request, *args, **kwargs):
        '''
        GET Method to retrieve Template resource
        through params..

        '''

        template_name = request.query_params.get('template_name', None)
        try:
            resource = TemplateResource.objects.get(
                template_name=template_name)
            serializers = TemplateResourceUpdateSerializer(resource)
            return Response({'status': True, "data": serializers.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND)
