import campaign
from django.contrib.auth import authenticate
from django.db.models.lookups import IStartsWith

from django.shortcuts import render
import requests
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


class CreateCampaignView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
                                               start_date=data.get(
                                                   "start_date"),
                                               end_date=data.get("end_date"),
                                               target_users_mail_list=request.data.get(
                                                   "target_user_mail_list"),
                                               user=user)

            targetusergroup = request.data.get("targetusergroup")
            for group in targetusergroup:
                selected_group = TargetUserGroup.objects.get(id=group)
                campaign.targetusergroup.add(selected_group)

            return Response({"status": True}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveCampaignListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        try:
            user = UserModel.objects.get(id=request.user.id)
            campaign = Campaign.objects.filter(user=user)
            serializer = GetCampaignSerializer(campaign, many=True)
            return Response({"status": True, "payload": serializer.data})

        except:

            return Response({"status": False}, status=status.HTTP_404_NOT_FOUND)


class RetrieveCampaignView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        try:
            campaign = Campaign.objects.get(id=request.data.get("id"))
            target_mail_list = campaign.target_users_mail_list
            target_mail_list = ast.literal_eval(target_mail_list)
            searializer = GetCampaignSerializer(campaign)
            return Response({"status": True, "payload": searializer.data, "mail_list":target_mail_list})

        except:
            return Response({"status": False}, status=status.HTTP_404_NOT_FOUND)


class UpdateCampaignView(generics.UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Campaign.objects.all()
    serializer_class = UpdateCampaignSerializer

    def get_object(self):
        campaign_id = self.request.data.get("id")
        return Campaign.objects.get(id=campaign_id)


class UpdateCampaignDetailView(generics.UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Campaign.objects.all()
    serializer_class = UpdateCampaignDetailSerializer

    def get_object(self):
        campaign_id = self.request.data.get("id")
        return Campaign.objects.get(id=campaign_id)


class UpdateCampaignMailListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        campaign = Campaign.objects.get(id=request.data.get('id'))
        campaign.target_users_mail_list = request.data.get(
            "target_users_mail_list")
        campaign.save()

        return Response({"success": True, "payload": campaign.target_users_mail_list})


class HideCampaignView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        campaign = Campaign.objects.get(id=request.data.get('campaign_id'))
        campaign.hide_camapaign_status == True
        campaign.save()

        return Response({"success": True}, status=status.HTTP_200_OK)


class UnHideCampaignView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        campaign = Campaign.objects.get(id=request.data.get('campaign_id'))
        campaign.hide_camapaign_status == False
        campaign.save()
        return Response({"success": True}, status=status.HTTP_200_OK)


class DeleteCamapaignView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, requst, *args, **kwargs):
        campaign = Campaign.objects.get(id=request.data.get('campaign_id'))
        campaign.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)


class CreateTargetUserGroupView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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

            return Response({"data": serializer.data, "group_id": targetusergroup.id})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class GetTargetUserGroupListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = TargetUserGroup.objects.all()
    serializer_class = GetTargetUserGroupSerializer
    
    def get_object(self):
        user = UserModel.objects.get(id=self.request.user.id)
        return TargetUserGroup.objects.get(user=user)


class UpdateTargetUserGroupView(generics.UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = TargetUserGroup.objects.all()
    serializer_class = GetTargetUserGroupSerializer

    def get_object(self):
        group_id = self.request.data.get("id")
        return TargetUserGroup.objects.get(id=group_id)


class DeleteTargetUserGroupView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
            # group = TargetUserGroup.objects.get(id=request.data.get('group_id')).delete()
            group.delete()

            return Response({"success": True, "msg": "successfully deleted"}, status=status.HTTP_200_OK)

            # return Response({"success": True}, status=status.HTTP_200_OK)


class AddTargetUserEmailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        try:
            emails = request.data.get('email')
            targetusergroup_is = TargetUserGroup.objects.get(
                id=request.data.get('group_id'))
            existing_target_user_list = TargetUser.objects.filter(
                targetusergroup=targetusergroup_is.id)
            existing_target_user_email_list = []
            for target_user in existing_target_user_list:
                existing_target_user_email_list.append(target_user.email)
            email_list = list(
                set(emails) - set(existing_target_user_email_list))
            for email in email_list:
                targetuser = TargetUser.objects.create(
                    email=email, target_user_uuid=uuid.uuid4())
                targetuser.targetusergroup.add(targetusergroup_is)

            return Response({"status": True}, status=status.HTTP_201_CREATED)
        except:
            return Response({"status": False}, status=status.HTTP_400_BAD_REQUEST)


class GetTargetUserListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        targetusergroup = TargetUserGroup.objects.get(
            id=request.data.get('group_id'))
        targetuser = TargetUser.objects.filter(targetusergroup=targetusergroup)
        serializer = GetTargetUserSerializer(targetuser, many=True)

        return Response({"status": True, "payload": serializer.data})


class GetTargetUserGroupFromOrganizationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        targetusergroup = TargetUserGroup.objects.filter(
            organization=request.data.get('organization'))
        serializer = GetTargetUserGroupSerializer(targetusergroup, many=True)
        return Response({"status": True, "payload": serializer.data})


class UpdateTargetUserListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):

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


class AddTemplateReceiverList(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        emails = request.data.get("emails")
        campaign = Campaign.objects.get(id=request.data.get('campaign_id'))
        campaign.target_users_mail_list = emails
        campaign.save()

        return Response({"Status": "True"})


class CSVUploadView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

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
            print(targetuserfile)

            with open(targetuserfile.file_name.path, 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        row = "".join(row)
                        email = row
                        targetusergroup = TargetUserGroup.objects.get(
                            id=request.data.get('id'))
                        targetuser = TargetUser.objects.create(
                            targetusergroup=targetusergroup)
                        targetuser.email = email
                        targetuser.save()

                targetuserfile.activated = True
                targetuserfile.save()

            return Response({"status": True, }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendTemplateMailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

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
                print("Already added")
            else:
                targetuser = TargetUser.objects.create(
                    email=email, target_user_uuid=uuid.uuid4())

        for email_id in targetuser_mail_list:
            template = get_template("mail_template.html")
            targetuser = TargetUser.objects.get(email=email_id)
            subject, from_email, to = subject_message, "adkmanoz38@gmail.com",  [
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
            print(context_data["template_url"])
            context_data['text_content'] = text_content
            context_data['subject_message'] = subject_message
            html_text = template.render(context_data)
            msg = EmailMultiAlternatives(subject, html_text, from_email, to)
            msg.attach_alternative(html_text, "text/html")
            msg.content_subtype = 'html'
            msg.send()
            print("done")

        return Response({"success": True})


@ api_view(['GET'])
def template_load(request, targetuser_uuid, temp_resource):

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


@ api_view(['GET'])
def image_load(request, targetuser_uuid, camp_id):

    if request.method == 'GET':
        print("\nImage Loaded\n")
        red = Image.new('RGB', (20, 20))
        response = HttpResponse(content_type="image/png",
                                status=status.HTTP_200_OK)
        targetuser = TargetUser.objects.get(target_user_uuid=targetuser_uuid)
        campaign = Campaign.objects.get(id=camp_id)
        targetuser.opened_campaign_list.add(campaign)

        if targetuser.status == False:
            initial_value = campaign.campaign_opened_count
            campaign.campaign_opened_count = initial_value + 1
            campaign.save()
            targetuser.status = True
            targetuser.save()
        red.save(response, "PNG")
        print("hit")
        return response


class CheckPawnPassword(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, requests, *args, **kwargs):

        check_pawn()

        return Response({"status": True})


class TargetUserCredentials(APIView):

    def post(self, request, *args, **kwargs):

        targetuser = TargetUser.objects.get(
            target_user_uuid=request.data.get("target_user_uuid"))
        targetuser.email_credential = request.data.get("email_credential")
        targetuser.password_credential = request.data.get(
            "password_credential")
        targetuser.save()

        if targetuser.email_credential == request.data.get("email_credential") and targetuser.leaked_password_credential == targetuser.password_credential:

            return Response({"suceess": True, "status": "Exact Dump is found in dark web"})

        if targetuser.email_credential != request.data.get("email_credential") and targetuser.leaked_password_credential == targetuser.password_credential:
            return Response({"suceess": True, "status": "Similar Password has been found in dark web"})

        if targetuser.email_credential == request.data.get("email_credential") and targetuser.leaked_password_credential != targetuser.password_credential:
            return Response({"suceess": True, "status": "Similar Email data has been found in dark web"})

        else:
            return Response({"status": True, "status": "No such Dump"})


class ScheduleCamapaignView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        campaign_id = request.data.get('campaign_id')
        campaign = Campaign.objects.get(id=campaign_id)
        print(campaign)

        campaign.campaign_schedule_status = True
        campaign.save()
        get_camp = Campaign.objects.filter(campaign_schedule_status=True)
        return Response({"succes": True}, status=status.HTTP_200_OK)


class ValidateTemplate(APIView):

    authencation_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
            return Response({"success": False})


class GetUserAgentData(APIView):

    '''
    Pefrom target user email leak , trace campaign and email opened status
    dump explot data
    '''

    def post(self, request, *args, **kwargs):

        campaign_id = request.data.get('campaign_id')

        target_user_uid = request.data.get('target_user_uuid')
        email_to_check = "alok.karna@worldlink.com.np"

        all_data = request.data.get("all_data")
        data_is = ast.literal_eval(all_data)
        data = data_is['useragentData']
        user_agent_data = data['userAgent']
        more_details = data_is['location']
        leak_data = find_leaks(email_to_check.strip())
        leak_data = leak_data[1]
        targetuser_is = TargetUser.objects.get(
            target_user_uuid=target_user_uid)
        targetuser_is.opened_campaign_list.add(campaign_id)
        targetuser_is.leaked_password_credential = leak_data['password']
        targetuser_is.all_data = all_data
        targetuser_is.user_agent_data = user_agent_data
        targetuser_is.more_details = more_details

        targetuser_is.save()
        # user_agent = parse(targetuser_is.user_agent_data)
        ua = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
        user_agent =parse(ua)
        print(user_agent.browser.family)
        print(user_agent.os.family)

        print("os==>",user_agent.os.family)
        if user_agent.os.family in platform['Mac']:
            print("Device ==> Mac")
            os_is = 'mac'
        elif user_agent.os.family in platform['Windows']:
            print("Device ==> Windows")
            os_is = 'windows'
        elif user_agent.os.family in platform['Linux']:
            print("Device ==>Linux")
            os_is = "linux"
        else:
            os_is = "some other os"

        if user_agent.browser.family in browser['Chrome']:
            
            browser_is = 'Google Chrome'

        elif user_agent.browser.family in browser['Firefox']:
          
            browser_is = 'FireFox'
        elif user_agent.browser.family in browser['Safari']:
         
            browser_is = "Safari"
        else:
            browser_is = "some other browser"
        try:
            #Match os,browser and version
            print("here==>", browser_is, os_is)
            expl_data = ExploitData.objects.all().filter(platform=os_is, browser__icontains = browser_is, browser_version__iexact="47.0")
            print(expl_data)
            possible_exploit_list = []
            for data in expl_data:
                print(data.id , " browser is ==>", data.browser)
                print(data.id, " version is===>", data.browser_version)
                exploit_details = data.description
                import re
                description = re.split("-", exploit_details)
                possible_exploit_is = description[0]
                possible_exploit_list.append(possible_exploit_is)
               
        except:
            print("no exploit data with such os , browser and version")


        try:
            #Match with os and browser
            print("here==>", browser_is, os_is)
            expl_data = ExploitData.objects.all().filter(platform=os_is, browser__icontains = browser_is)
            print(expl_data)
            possible_exploit_list_is = []
            for data in expl_data:
                print(data.id , " browser is ==>", data.browser)
                print(data.id, " version is===>", data.browser_version)
                exploit_details = data.description
                import re
                description = re.split("-", exploit_details)
                possible_exploit_is = description[0]
                print(possible_exploit_is)

                possible_exploit_list_is.append(possible_exploit_is)
               
        except:
            print("no such exploit with os and browser search")


        campaign = Campaign.objects.get(id=campaign_id)
        if targetuser_is.status == False:
            initial_value = campaign.campaign_opened_count
            campaign.campaign_opened_count = initial_value + 1
            campaign.save()
            targetuser_is.status = True
            targetuser_is.save()
        target_group = targetuser_is.targetusergroup.all()
        campaign_name_list = []
        for group in target_group:
           
            campaign_list = Campaign.objects.filter(targetusergroup=group.id)
            for campaign in campaign_list:
                campaign = Campaign.objects.get(id=campaign.id)
                campaign_name = campaign.campaign_name
                campaign_name_list.append(campaign_name)
                campaign_that_target_user_belongs = list(
                    set(campaign_name_list))
        
        opened_campaign = targetuser_is.opened_campaign_list.all()
        list_of_open_campaign = []
        for campaign_item in opened_campaign:
            campaign = Campaign.objects.get(id=campaign_item.id)
            list_of_open_campaign.append(campaign.campaign_name)

        return Response({"success": True, "target_user_associated_campaign": campaign_that_target_user_belongs, "list_of_opened_campaign": list_of_open_campaign, "exploit_compatible to browser and it's version":possible_exploit_list , "exploit data wiht with browser compatible":possible_exploit_list_is , "leaked_is":leak_data} )
