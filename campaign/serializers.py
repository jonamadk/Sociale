import re
from django.contrib.auth.models import User
import campaign
from group import serializer
from django.db.models import fields
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

#### Target User Serializers
class CreateTargetUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(
        TargetUser.objects.all())], max_length=None, required=True)

    class Meta:
        model = TargetUser
        fields = ['email']

#### Get Target User Serializer
class GetTargetUserSerializer(serializers.ModelSerializer):
    
    

    class Meta:
        model = TargetUser
        fields = '__all__'
        
    
 

#### Target User Group Serializers
class CreateTargetUserGroupSerializer(serializers.ModelSerializer):

    class Meta:

        model = TargetUserGroup
        fields = ['group_name', 'department', 'organization']

#### Get Target User Group Serializer
class GetTargetUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetUserGroup
        fields = '__all__'

#### Campaign Serializers
class CreateCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['campaign_name', 'campaign_title',
                  'templateresource', 'start_date', 'end_date']

#### Update Campaign Serializer
class UpdateCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['campaign_name', 'campaign_title', 'templateresource',
                  'start_date', 'end_date', 'id', 'targetusergroup']

#### Update Campaign Detail Serializer
class UpdateCampaignDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['campaign_name', 'campaign_title',
                  'templateresource', 'start_date', 'end_date', 'id']
        
#### Get Campaign Serializer

class GetCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = '__all__'

#### CSV Upload Serializer
class CSVUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetUserCSV
        fields = ['file_name']

from collections import Counter
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
        data_is = []
        targetuser_leaked = TargetUser.objects.filter(associated_campaign_list__id=obj.id, password_leaked_status=True)
        for targetuser in targetuser_leaked:
            data_is.append(targetuser)

        leaked_user_count_is =len(data_is)
        return leaked_user_count_is





               

class GetLeakedUserReportSerializer(serializers.ModelSerializer):
    campaign_name = serializers.SerializerMethodField(method_name = 'get_campaign')
    
    
    class Meta:
        model = TargetUser
        fields = ['id','email','browser', 'operating_sys','password_leaked_status', 'password_credential', 'email_credential','user_agent_data','leaked_password_credential', 'campaign_name']
    
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



class GetTargetUserExploitSerializer(serializers.ModelSerializer):
    possible_exploit = serializers.SerializerMethodField(method_name = 'find_possible_exploit')
    
    
    class Meta:
        model = TargetUser
        fields =['id','email','password_leaked_status','operating_sys','browser','leaked_password_credential','email_credential','password_credential','possible_exploit']
    
    
    
        
    def find_possible_exploit(self , obj):
        
        targetusers = TargetUser.objects.filter(id = obj.id )
        possible_exploit_list = []
        for targetuser in targetusers:
            try:
                user_agent = parse(targetuser.user_agent_data)
           
            
                for key , value in platform.items():
                    if user_agent.os.family in platform[key]:
                        os_is = key
                
                for key , value in browser.items():
                    if user_agent.browser.family in browser[key]:
                        browser_is = key
            
                                
                try:
                    expl_data_version_match = ExploitData.objects.all().filter(
                    platform=os_is, browser__icontains=browser_is, browser_version__iexact=user_agent.browser.version_string)
                            
                    if len(expl_data_version_match) ==0:
                        expl_data_match = ExploitData.objects.all().filter(
                                    platform=os_is, browser__icontains=browser_is)
                        expl_data = expl_data_match
                    else:
                        expl_data = expl_data_version_match
                    for data in expl_data:
                        exploit_details = data.description
                        import re
                        description = re.split("-", exploit_details)
                        possible_exploit_is = description[0]
                        possible_exploit_list.append(possible_exploit_is)
                            
                    return possible_exploit_list
                except:
                    return possible_exploit_list
            except:
                pass 
                
                
            
        