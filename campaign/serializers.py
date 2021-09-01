import campaign
from group import serializer
from django.db.models import fields
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.db.models import Count
from rest_framework import status




class CreateTargetUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(
        TargetUser.objects.all())], max_length=None, required=True)

    class Meta:
        model = TargetUser
        fields = ['email']


class GetTargetUserSerializer(serializers.ModelSerializer):
    
    

    class Meta:
        model = TargetUser
        fields = '__all__'
        
    
 

    

class CreateTargetUserGroupSerializer(serializers.ModelSerializer):

    class Meta:

        model = TargetUserGroup
        fields = ['group_name', 'department', 'organization']


class GetTargetUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetUserGroup
        fields = '__all__'


class CreateCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['campaign_name', 'campaign_title',
                  'templateresource', 'start_date', 'end_date']


class UpdateCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['campaign_name', 'campaign_title', 'templateresource',
                  'start_date', 'end_date', 'id', 'targetusergroup']


class UpdateCampaignDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['campaign_name', 'campaign_title',
                  'templateresource', 'start_date', 'end_date', 'id']


class GetCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = '__all__'


class CSVUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetUserCSV
        fields = ['file_name']


class CountTargetUserDatewiseCountSerializer(serializers.ModelSerializer):
    target_user_count_by_date = serializers.SerializerMethodField(method_name = 'get_count')
    leaked_user_count_is = serializers.SerializerMethodField(method_name = 'get_leaked')
    class Meta:
        model = Campaign
        fields = ['id','campaign_name','target_user_count_by_date','campaign_opened_count','leaked_user_count_is']
        
    
    def get_count(self, obj):
        
        data_is = []
        details = CampaignStatus.objects.filter(campaign_id = obj.id).values('campaign_opened_date').annotate(total_count = Count('campaign_opened_date')) 
        for campaignstatus in details:
            data_dict = {}
            data_dict["date"] = campaignstatus.get('campaign_opened_date')
            data_dict["count"] = campaignstatus.get('total_count')
        
            data_is.append(data_dict)
       
        
            return data_is
        else:
            return data_is
    
    def get_leaked(self, obj):
        targetuser_leaked = TargetUser.objects.filter(associated_campaign_list__id=obj.id, password_leaked_status=True).values('password_leaked_status').annotate(total_Leakedtargetuser_count =Count('password_leaked_status'))
   
        return targetuser_leaked

        

class GetLeakedUserReportSerializer(serializers.ModelSerializer):
    campaign_name = serializers.SerializerMethodField(method_name = 'get_campaign')

    
    
    class Meta:
        model = TargetUser
        fields = ['id','email','browser', 'operating_sys','password_leaked_status','user_agent_data','leaked_password_credential', 'campaign_name', ]
    
    def get_campaign(self, obj):
        targetusers = TargetUser.objects.filter(id = obj.id)
        campaign_name_list = {}
        
        associated_campaign_list = []
        opened_campaign_List = []
        for targetuser in targetusers:
            
            associated_campaigns = Campaign.objects.filter(id__in = targetuser.associated_campaign_list.all())
            opened_campaigns = Campaign.objects.filter(id__in = targetuser.opened_campaign_list.all())
            for campaign in associated_campaigns: 
                associated_campaign_list.append(campaign.campaign_name)
                campaign_name_list["assocaited"] = associated_campaign_list
            for campaign in opened_campaigns:
                opened_campaign_List.append(campaign.campaign_name)
                campaign_name_list["opened"] = opened_campaign_List

        return campaign_name_list
                
            
        
class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogger
        fields = "__all__"
        
        
    
class RetrieveCamapaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['campaign_name']



        