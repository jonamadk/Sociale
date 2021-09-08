
from os import name
from typing import Counter
from django.core.exceptions import AppRegistryNotReady
from django.db.models import manager
from django.db.models.expressions import F
from django.urls.conf import path
from group import serializer
import campaign
from django.contrib.auth import authenticate
from django.db.models.lookups import GreaterThan, IStartsWith
from django.shortcuts import render
import requests
from group import permissions
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from user.models import UserModel
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
import csv
import json
import uuid
from django.http import HttpResponse, HttpRequest, request
from PIL import Image
from rest_framework.decorators import api_view
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from .pawndb import check_pawn, find_leaks
from decouple import config
from django.conf import settings
from template.serializers import *
import ast
from group.permissions import *
from .models import*
from user_agents import parse
from exploit_data.models import ExploitData
from .exploit_match import *
from exploit_data.serializers import *
from group.permissions import has_permission
from datetime import date
from collections import Counter
from django.db.models import Count
from campaign import exploit_match
from user.logger import logger_is
from .pagination import *
from user.logmessage import *



class CreateCampaignView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaign.add_campaign')
    def post(self, request, *args, **kwargs):

        serializer = CreateCampaignSerializer(data=request.data)
        user = UserModel.objects.get(id=request.user.id)

        if serializer.is_valid():
            data = serializer.validated_data
            campaign = Campaign.objects.create(campaign_name=data.get("campaign_name"),
                                               campaign_title=data.get(
                                                   "campaign_title"),
                                               templateresource=data.get(
                                                   "templateresource"),
                                               target_users_mail_list=request.data.get(
                                                   "target_user_mail_list"),
                                               user=user)

            targetusergroup = request.data.get("targetusergroup")
            for group in targetusergroup:
                selected_group = TargetUserGroup.objects.get(id=group)
                campaign.targetusergroup.add(selected_group)
            
            target_mail_list = campaign.target_users_mail_list
            # target_mail_list = ast.literal_eval(target_mail_list)

            
            print(target_mail_list)
            targetuser_mail_list = []
            for item in range(0, len(target_mail_list)):
                item_dictionary = target_mail_list[item]
                item_email = item_dictionary['email']
                targetuser_mail_list.append(item_email)
            
            targetusergroup = campaign.targetusergroup.all()
            for group in targetusergroup:

                group_is = TargetUserGroup.objects.get(id=group.id)
                targetuser = group_is.targetuser.all()
                email_list = []
                for user in targetuser:
                    email = user.email
                    email_list.append(email)
            new_added_mail_list = [
                x for x in targetuser_mail_list if x not in email_list]
            all_target_user = TargetUser.objects.all()
            all_email_list = []
            for user in all_target_user:
                email = user.email
                all_email_list.append(email)
            for email in new_added_mail_list:
                if email in all_email_list:
                    pass
                else:
                    targetuser = TargetUser.objects.create(
                            email=email, target_user_uuid=uuid.uuid4())
                    targetuser.associated_campaign_list.add(campaign)

            return Response({"status": True}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveCampaignListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaign.view_campaign')
    def get(self, request, *args, **kwargs):

        try:
            user = UserModel.objects.get(id=request.user.id)
            campaign = Campaign.objects.filter(user=user)
            serializer = GetCampaignSerializer(campaign, many=True)
            return Response({"status": True, "payload": serializer.data}, status=status.HTTP_200_OK)

        except:

            return Response({"status": False}, status=status.HTTP_404_NOT_FOUND)


class RetrieveAllCampaignsFromOrganization(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    queryset = Campaign.objects.all()
    serializer_class = GetCampaignSerializer


class RetrieveCampaignView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission("campaign.view_campaign")
    def post(self, request, *args, **kwargs):
        try:
            campaign = Campaign.objects.get(id=request.data.get("id"))
            target_mail_list = campaign.target_users_mail_list
            target_mail_list = ast.literal_eval(target_mail_list)
            searializer = GetCampaignSerializer(campaign)
            return Response({"status": True, "payload": searializer.data, "mail_list": target_mail_list})

        except:
            return Response({"status": False}, status=status.HTTP_404_NOT_FOUND)


class UpdateCampaignView(generics.UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    queryset = Campaign.objects.all()
    serializer_class = UpdateCampaignSerializer

    def get_object(self):
        campaign_id = self.request.data.get("id")
        return Campaign.objects.get(id=campaign_id)


class UpdateCampaignDetailView(generics.UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    queryset = Campaign.objects.all()
    serializer_class = UpdateCampaignDetailSerializer

    def get_object(self):
        campaign_id = self.request.data.get("id")
        return Campaign.objects.get(id=campaign_id)


class UpdateCampaignMailListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaign.change_campaign')
    def put(self, request, *args, **kwargs):
        try:
            campaign = Campaign.objects.get(id=request.data.get('id'))
            campaign.target_users_mail_list = request.data.get(
                "target_users_mail_list")
            campaign.save()

            return Response({"success": True, "payload": campaign.target_users_mail_list})
        except:
            return Response({"success":False}, status=status.HTTP_400_BAD_REQUEST)

class HideCampaignView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        
        try:
            campaign = Campaign.objects.get(id=request.data.get('campaign_id'))
            campaign.hide_camapaign_status == True
            campaign.save()

            return Response({"success": True}, status=status.HTTP_200_OK)
        except:
            return Response({"success":False}, status=status.HTTP_400_BAD_REQUEST)

class UnHideCampaignView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            campaign = Campaign.objects.get(id=request.data.get('campaign_id'))
            campaign.hide_camapaign_status == False
            campaign.save()
            return Response({"success": True}, status=status.HTTP_200_OK)
        except:
            return Response({"success":False}, status=status.HTTP_400_BAD_REQUEST)


class DeleteCamapaignView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaign.delete_campaign')
    def delete(self, request, *args, **kwargs):
        try:
            campaign = Campaign.objects.get(id=request.data.get('campaign_id'))
            campaign.delete()
            return Response({"success": True}, status=status.HTTP_200_OK)
        except:
            return Response({"success":False}, status=status.HTTP_400_BAD_REQUEST)
        

class CreateTargetUserGroupView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaign.add_targetusergroup')
    def post(self, request, *args, **kwargs):
        serializer = CreateTargetUserGroupSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = UserModel.objects.get(id=request.user.id)
            targetusergroup = TargetUserGroup.objects.create(group_name=data.get('group_name'),
                                                             department=data.get(
                                                                 'department'),
                                                             organization=data.get(
                                                                 'organization'),
                                                             user=user)

            return Response({"data": serializer.data, "group_id": targetusergroup.id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTargetUserGroupListView(generics.ListAPIView):

    '''

    Returns the list of the target-user group 

    according to the user

    '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    queryset = TargetUserGroup.objects.all()
    serializer_class = GetTargetUserGroupSerializer

    def get_object(self):
        user = UserModel.objects.get(id=self.request.user.id)
        return TargetUserGroup.objects.get(user=user)


class GetTargetUserGroupFromOrganizationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaigm.view_targetusergroup')
    def post(self, request, *args, **kwargs):
        try:
            targetusergroup = TargetUserGroup.objects.filter(
                organization=request.data.get('organization'))
            serializer = GetTargetUserGroupSerializer(targetusergroup, many=True)
            return Response({"status": True, "payload": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"status": False}, status=status.HTTP_400_BAD_REQUEST)

class GetTargetUserGroupAllView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = TargetUserGroup.objects.all()
    serializer_class = GetTargetUserGroupSerializer


class UpdateTargetUserGroupView(generics.UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = TargetUserGroup.objects.all()
    serializer_class = GetTargetUserGroupSerializer

    def get_object(self):
        group_id = self.request.data.get("id")
        return TargetUserGroup.objects.get(id=group_id)


class DeleteTargetUserGroupView(APIView):

    '''
    Deletes the target-user group if group is not
    associated in any campaign

    '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaign.delete_targetusergroup')
    def delete(self, request, *args, **kwargs):

        group = TargetUserGroup.objects.get(id=request.data.get('group_id'))
        group_id = group.id

        campaign_list = Campaign.objects.filter(targetusergroup=group_id)
        if campaign_list.exists():

            campaign_name_list = []
            errormessage = {}
            for campaign in campaign_list:
                print("done")
                print(campaign)
                campaign_name = campaign.campaign_name
                campaign_name_list.append(campaign_name)

            errormessage["Cannot remove, since groups are used in following campaigns"] = campaign_name_list

            return Response({"success": False, "msg": errormessage}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            
            group.delete()

            return Response({"success": True, "msg": "successfully deleted"}, status=status.HTTP_200_OK)

           


class AddTargetUserEmailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        POST Method to add the target users in 
        targetuser group
        
        Post list of email to be added to the group_id 
        of the targetuser group
        
        '''

        try:
        
            
            emails = request.data.get('email')
            group_id = request.data.get('group_id')
            targetusergroup_is = TargetUserGroup.objects.get(
                id=group_id)

            existing_target_user_list = TargetUser.objects.filter(
                targetusergroup=targetusergroup_is.id)

            existing_target_user_email_list = []

            for target_user in existing_target_user_list:
                existing_target_user_email_list.append(target_user.email)

            for email in emails:

                if email in existing_target_user_email_list:
                    pass
                else:
                    targetuser = TargetUser.objects.create(
                        email=email, target_user_uuid=uuid.uuid4())
                    targetuser.targetusergroup.add(targetusergroup_is)

                    # email_to_check = email

           
                    # leak_data = find_leaks(email_to_check.strip())
                    # leak_data = leak_data[1]
    
                    # targetuser.leaked_password_credential = leak_data['password']
                    # targetuser.save()
            
            return Response({"status": True}, status=status.HTTP_201_CREATED)
        except:
            return Response({"status": False}, status=status.HTTP_400_BAD_REQUEST)


class GetTargetUserListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaign.add_targetuser')
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            targetusergroup = TargetUserGroup.objects.get(
                id=request.data.get('group_id'))
            targetuser = TargetUser.objects.filter(targetusergroup=targetusergroup)
            serializer = GetTargetUserSerializer(targetuser, many=True)
        

            return Response({"status": True, "payload": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"status":False}, status=status.HTTP_400_BAD_REQUEST)
            


class GetAllTargetUsersList(APIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            targetuserslist = TargetUser.objects.all()
            serializer = GetTargetUserSerializer(targetuserslist, many = True)
            
            return Response({"Status":True, "payload":serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"status":False}, status=status.HTTP_400_BAD_REQUEST)

class UpdateTargetUserListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaign.change_targetuser')
    def put(self, request, *args, **kwargs):
        
        try:

            targetusergroup_is = TargetUserGroup.objects.get(
                id=request.data.get('group_id'))
            existing_target_user_list = TargetUser.objects.filter(
                targetusergroup=targetusergroup_is.id)
            target_user_id_list_to_remove = request.data.get("to_remove")
            for targetuser_id in target_user_id_list_to_remove:
                delete_target_user = TargetUser.objects.filter(
                    id=targetuser_id).delete()

            existing_target_user_email_list = []
            for target_user in existing_target_user_list:
                existing_target_user_email_list.append(target_user.email)
            emails = request.data.get('email')
            email_list = list(set(emails) - set(existing_target_user_email_list))
            for email in email_list:
                targetuser = TargetUser.objects.create(
                    email=email, target_user_uuid=uuid.uuid4())
                targetuser.targetusergroup.add(targetusergroup_is)

            return Response({"status": True}, status=status.HTTP_201_CREATED)
        except:
            return Response({"status":False}, status=status.HTTP_400_BAD_REQUEST)


class AddTemplateReceiverList(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @has_permission('campaign.change_campaign')
    def post(self, request, *args, **kwargs):
        
        try:

            emails = request.data.get("emails")
            campaign = Campaign.objects.get(id=request.data.get('campaign_id'))
            campaign.target_users_mail_list = emails
            campaign.save()

            return Response({"status":True}, status=status.HTTP_200_OK)
        except:
            return Response({"status":False}, status=status.HTTP_400_BAD_REQUEST)


        

class CSVUploadView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @has_permission('campaign.add_targetuser')
    def post(self, request, *args, **kwargs):
        '''
        POST Method for uploading the CSV

        '''
        serializer = CSVUploadSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            targetusercsv = TargetUserCSV.objects.create(
                file_name=data.get("file_name"))
            targetuserfile = TargetUserCSV.objects.get(activated=False)
            with open(targetuserfile.file_name.path, 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        row = "".join(row)
                        email = row
                        targetusergroup_is = TargetUserGroup.objects.get(
                            id=request.data.get('id'))
                        try:
                            print(email)
                            targetuser = TargetUser.objects.get(email = email)
                        except:
                            
                            targetuser= TargetUser.objects.create(email = email, target_user_uuid = uuid.uuid4())
                            targetuser.targetusergroup.add(targetusergroup_is)
                            
                            # email_to_check = email

           
                            # leak_data = find_leaks(email_to_check.strip())
                            # leak_data = leak_data[1]
         
                            # targetuser.leaked_password_credential = leak_data['password']
                            # targetuser.save()

                targetuserfile.activated = True
                targetuserfile.save()

            return Response({"status": True, }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SendTemplateMailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        
        try:

            campaign_id = request.data.get("id")
            body_message = request.data.get("body_message")
            subject_message = request.data.get("subject_message")

            campaign = Campaign.objects.get(id=campaign_id)
            target_mail_list = campaign.target_users_mail_list
            target_mail_list = ast.literal_eval(target_mail_list)

            targetuser_mail_list = []
            for item in range(0, len(target_mail_list)):
                item_dictionary = target_mail_list[item]
                item_email = item_dictionary['email']
                targetuser_mail_list.append(item_email)


            for email_id in targetuser_mail_list:
                template = get_template("mail_template.html")
                targetuser = TargetUser.objects.get(email=email_id)
                subject, from_email, to = subject_message, "postmaster@manojadhikary.com.np",  [
                    email_id]
                text_content = body_message
                context_data = dict()
                context_data["image_url"] = request.build_absolute_uri(
                    ("image_load"))
                print(context_data["image_url"])
                url_is = context_data["image_url"]+"/" + \
                    str(targetuser.target_user_uuid)+"/"+str(campaign.id)+"/"
                template_is = TemplateResource.objects.get(
                    template_name=campaign.templateresource)
                template_url = template_is.template_url + "/" + \
                    str(targetuser.target_user_uuid)+"/"+str(campaign.id) + \
                    "/"+str(campaign.templateresource)+"/"
                context_data["template_url"] = template_url
                context_data['url_is'] = url_is
                context_data['text_content'] = text_content
                context_data['subject_message'] = subject_message
                html_text = template.render(context_data)
                msg = EmailMultiAlternatives(subject, html_text, from_email, to)
                msg.attach_alternative(html_text, "text/html")
                msg.content_subtype = 'html'
                msg.send()
                print("done")

            return Response({"success": True}, status=status.HTTP_200_OK)
        except:
            return Response({"success":False}, status=status.HTTP_400_BAD_REQUEST)
            


@api_view(['GET'])
def template_load(request, targetuser_uuid, temp_resource):
    
    try:
        if request.method == 'GET':
            targetuser = TargetUser.objects.get(target_user_uuid=targetuser_uuid)
            email_to_check = "alok.karna@worldlink.com.np"
            print(email_to_check)
            leak_data = find_leaks(email_to_check.strip())
            leak_data = leak_data[1]
            targetuser.leaked_password_credential = leak_data['password']
            targetuser.save()
            resource = TemplateResource.objects.get(template_name=temp_resource)
            serializer = TemplateResourceUpdateSerializer(resource)

            return Response({"targetuser_uuid": targetuser_uuid, "Data": serializer.data, "leak_data": leak_data})
    except:
        return Response({"success":False}, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET'])
def image_load(request, targetuser_uuid, camp_id):
    try:

        if request.method == 'GET':
            print("\nImage Loaded\n")
            red = Image.new('RGB', (20, 20))
            response = HttpResponse(content_type="image/png",
                                    status=status.HTTP_200_OK)
            targetuser = TargetUser.objects.get(target_user_uuid=targetuser_uuid)
            campaign = Campaign.objects.get(id=camp_id)
            targetuser.opened_campaign_list.add(campaign)
            campaignstat = CampaignStatus.objects.filter(campaign = campaign , targetuser = targetuser)
            if campaignstat.exists():
                for campaignstatobject in campaignstat:
                    campaignstatobject.campaign_date = date.today()
                    campaignstatobject.save()
            
            else:
                CampaignStatus.objects.create(campaign = campaign ,targetuser = targetuser, campaign_opened_date = date.today())
            if targetuser.campaign_opened_status == False:
                initial_value = campaign.campaign_opened_count
                campaign.email_opened_status = True
                campaign.campaign_opened_count = initial_value + 1
                campaign.save()
                targetuser.campaign_opened_status = True
                targetuser.save()
            red.save(response, "PNG")
            print("hit")
            return response
    except:
        return Response({"success":False}, status=status.HTTP_400_BAD_REQUEST)


class TargetUserCredentials(APIView):

    def post(self, request, *args, **kwargs):

        targetuser = TargetUser.objects.get(
            target_user_uuid=request.data.get("target_user_uuid"))
        targetuser.email_credential = request.data.get("email_credential")
        targetuser.password_credential = request.data.get(
            "password_credential")
        targetuser.save()

        if targetuser.email == request.data.get("email_credential") and targetuser.leaked_password_credential == targetuser.password_credential:

            return Response({"suceess": True, "status": "Exact Dump is found in dark web"})

        if targetuser.email != request.data.get("email_credential") and targetuser.leaked_password_credential == targetuser.password_credential:
            return Response({"suceess": True, "status": "Similar Password has been found in dark web"})

        if targetuser.email == request.data.get("email_credential") and targetuser.leaked_password_credential != targetuser.password_credential:
            return Response({"suceess": True, "status": "Similar Email data has been found in dark web"})

        else:
            return Response({"status": True, "status": "No such Dump"})


# class ScheduleCamapaignView(APIView):

#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         campaign_id = request.data.get('campaign_id')
#         campaign = Campaign.objects.get(id=campaign_id)
#         campaign.campaign_schedule_status = True
#         campaign.save()
#         get_camp = Campaign.objects.filter(campaign_schedule_status=True)
#         return Response({"succes": True}, status=status.HTTP_200_OK)


class ValidateTemplate(APIView):

    def post(self, request, *args, **kwargs):

        target_user_uuid = request.data.get('target_user_uuid')
        campaign_id = request.data.get('campaign_id')
        template_resource = request.data.get('template_name')

        try:
            campaign = Campaign.objects.get(id=campaign_id)
            if campaign:
                target_user_uuid = TargetUser.objects.get(
                    target_user_uuid=target_user_uuid)
                if target_user_uuid:
                    template_resource = TemplateResource.objects.get(
                        template_name=template_resource)
                    if template_resource:
                        serializer = TemplateResourceUpdateSerializer(
                            template_resource)
                        return Response({"sucess": True, "data": serializer.data})
                    else:
                        return Response({"msg": "Template resource not matched"})
                else:

                    return Response({"msg": "TargetUser UUID not matched"})
            else:
                return Response({"msg": "Campaign not matched"})

        except:
            return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)


class GetUserAgentData(APIView):

    '''
    Pefrom target user email leak , trace campaign and email opened status
    dump explot data
    '''

    def post(self, request, *args, **kwargs):
        
        
        try:

            campaign_id = request.data.get('campaign_id')

            target_user_uid = request.data.get('target_user_uuid')

            email_to_check = "alok.karna@worldlink.com.np"

            user_agent_data = request.data.get("user_agent_data")
            # leak_data = find_leaks(email_to_check.strip())
            # leak_data = leak_data[1]
            targetuser_is = TargetUser.objects.get(
                target_user_uuid=target_user_uid)

            targetuser_is.opened_campaign_list.add(campaign_id)
            # targetuser_is.leaked_password_credential = leak_data['password']
            

            if targetuser_is.leaked_password_credential is None:
                targetuser_is.password_leaked_status = False
            else:
                targetuser_is.password_leaked_status = True
                
            targetuser_is.user_agent_data = user_agent_data
            user_agent = parse(user_agent_data)
            targetuser_is.browser = user_agent.browser.family
            targetuser_is.operating_sys= user_agent.os.family
            targetuser_is.save()

            campaign = Campaign.objects.get(id=campaign_id)
            targetuser_is.opened_campaign_list.add(campaign)
            if targetuser_is.campaign_opened_status == False:
                initial_value = campaign.campaign_opened_count
                campaign.campaign_opened_count = initial_value + 1
                campaign.save()
                targetuser_is.campaign_opened_status = True
                targetuser_is.save()
            campaignstat = CampaignStatus.objects.filter(campaign = campaign , targetuser = targetuser_is)
            if campaignstat.exists():
                for campaignstatobject in campaignstat:
                    campaignstatobject.campaign_date = date.today()
                    campaignstatobject.save()
            else:  
                CampaignStatus.objects.create(campaign = campaign ,targetuser = targetuser_is, campaign_opened_date = date.today())            
                return Response({"success": True, "leaked_is":"leak_data"}, status=status.HTTP_200_OK)
        except:
            return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)
            
    


class GetBrowserandOSData(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def post(self , request , *args, **kwargs):
        '''
        
        Post Method for retrieving browser and Operating 
        System Data 
        
        '''
        try:
            campaign_id = request.data.get('campaign_id')
            if campaign_id:
                targetusers_browser = TargetUser.objects.filter(associated_campaign_list__id=campaign_id).values('browser').annotate(total_browser_count = Count('browser'))
                targetusers_os = TargetUser.objects.filter(associated_campaign_list__id=campaign_id).values('operating_sys').annotate(total_os_count = Count('operating_sys'))
                targetuser_leaked = TargetUser.objects.filter(associated_campaign_list__id=campaign_id, password_leaked_status = True)
                targetusers = TargetUser.objects.filter(associated_campaign_list__id=campaign_id)
                campaigns = Campaign.objects.filter(id = campaign_id).values('campaign_opened_count')
        

            else:
                targetusers_browser = TargetUser.objects.values('browser').annotate(total_browser_count = Count('browser'))
                targetusers_os = TargetUser.objects.values('operating_sys').annotate(total_os_count = Count('operating_sys'))
                targetuser_leaked = TargetUser.objects.filter(password_leaked_status = True)
                targetusers = TargetUser.objects.all()
                campaigns = Campaign.objects.all().values('campaign_opened_count')
                
            data_list_browser = []
            detail ={}
            if targetusers_browser.exists():
                for targetuser in targetusers_browser:
                    data_list_browser
                    data = {}
                    data['browser name'] =targetuser.get('browser')
                    data['total browser count'] = targetuser.get('total_browser_count')
                    data_list_browser.append(targetuser)
                    detail["browsers"]=data_list_browser
            else:
                detail["browsers"] = data_list_browser
                
            data_list_os=[]
            if targetusers_os.exists():
                for targetuser in targetusers_os:
                    data = {}
                    data['operating sys name'] = targetuser.get('operating_sys')
                    data['total os count']=targetuser.get('total_os_count')
                    data_list_os.append(data)
                    detail["operating system"]=data_list_os
            else:
                detail["operating system"]=data_list_os
                
            leaked_targetuser_list = []
            for targetuser in targetuser_leaked:
                leaked_targetuser_list.append(targetuser.email)
            victim_count = len(leaked_targetuser_list)
            detail["total victim"] = victim_count
            
            
            targeruser_list=[]
            for targetuser in targetusers:
                targeruser_list.append(targetuser.email)
                
            target_user_count = len(targeruser_list)
            detail["total targetuser"] = target_user_count
            
            value_is = []
            for campaign in campaigns:
                value_is.append(campaign.get('campaign_opened_count'))
            sum_is = sum(value_is)
            detail["total opened"] = sum_is
            
            return Response({"status":True, 'data':detail}, status=status.HTTP_201_CREATED)
        except:
            return Response({"status":False}, status=status.HTTP_400_BAD_REQUEST)
            


    
class CountTargetUserDatewiseCountView(generics.ListAPIView):
    
    serializer_class = CountTargetUserDatewiseCountSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Campaign.objects.all()
    pagination_class = CamapaignDashboardpagination
    
    def get_queryset(self):
        campaign_id = self.request.GET.get('campaign',None)
        if campaign_id:
            return Campaign.objects.filter(id=campaign_id)
        return Campaign.objects.all()
            
    
        
class LeakedTargetuserData(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    queryset = TargetUser.objects.all()
    serializer_class = GetTargetUserSerializer
    pagination_class = Targetuserleakedpagination
    
    def get_queryset(self):
        campaign_id = self.request.GET.get('campaign',None)
        if campaign_id:
            return TargetUser.objects.filter(associated_campaign_list__id = campaign_id,password_leaked_status=True )
        return TargetUser.objects.filter(password_leaked_status=True)
    
    

class TargetuserReport(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = TargetUser.objects.all()
    serializer_class = GetLeakedUserReportSerializer
    pagination_class = TargetuserReportPagination
    def get_queryset(self):
        '''
        GET Method for targetuser filtered by Campaign 
        and with no filter
        '''
        campaign_id = self.request.GET.get('campaign',None)
        if campaign_id:
            return TargetUser.objects.filter(associated_campaign_list__id = campaign_id)
        return TargetUser.objects.all()
    
    
   
class CampaignListRetrieveAPI(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class =  RetrieveCamapaignSerializer
    queryset = Campaign.objects.all()
   
   
            
class TestForTorOne(APIView):

    def post(self, request, *args, **kwargs):

        email = request.data.get('email')
        leak_data = find_leaks(email.strip())
        leak_data = leak_data[1]

        return Response({"success": True, "msg": "from pawndb, ip in prox", "data": leak_data})



class ScheduleCampaignEmail(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def patch(self, request, *args, **kwargs):
        
        campaign_id = request.data.get("campaign_id")
        campaign = Campaign.objects.get(id=campaign_id)
        campaign_schedule_status = request.data.get("campaign_schedule_status")
        try:
            if campaign_schedule_status == True:
                campaign.campaign_schedule_status = True
                campaign.campaign_email_detail_message= request.data.get("campaign_email_detail_message")
                campaign.camapign_email_title_message= request.data.get("campaign_email_title_message")
                campaign.start_date =request.data.get("start_date")
                campaign.start_time =request.data.get("start_time")
                campaign.save()
            return Response({"success":True}, status=status.HTTP_200_OK)
        except:
            return Response({"success":True}, status=status.HTTP_400_BAD_REQUEST)
            
    



        
            
        
        
    
        
    
    