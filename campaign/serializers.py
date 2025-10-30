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
