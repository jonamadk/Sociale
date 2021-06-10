from django.db.models import fields
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator


class CreateTargetUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(TargetUser.objects.all())], max_length = None , required =True)

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
        fields = ['campaign_name', 'campaign_title', 'templateresource','start_date', 'end_date']


class UpdateCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['campaign_name', 'campaign_title', 'templateresource','start_date', 'end_date' ,'id' ,'targetusergroup']


class GetCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = '__all__'


class CSVUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetUserCSV
        fields = ['file_name']



