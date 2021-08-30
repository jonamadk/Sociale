import campaign
from group import serializer
from django.db.models import fields
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.db.models import Count

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
            data = {}
            data["date"] = campaignstatus.get('campaign_opened_date')
            data["count"] = campaignstatus.get('total_count')
        
            data_is.append(data)
       
        
        return data_is
    
    def get_leaked(self, obj):
        targetuser_leaked = TargetUser.objects.filter(password_leaked_status=True).values('password_leaked_status').annotate(total_Leakedtargetuser_count =Count('password_leaked_status'))
        leaked_data = []
        for targetuser in targetuser_leaked:
            data = targetuser.get('total_Leakedtargetuser_count')
           
            
        return data
        
    