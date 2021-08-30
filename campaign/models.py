
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields.reverse_related import OneToOneRel
from template.models import TemplateResource
from user.models import UserModel
# Create your models here.


class TargetUserGroup(models.Model):

    group_name = models.CharField(max_length=254, null=True, blank=True)
    department = models.CharField(max_length=254, null=True, blank=True)
    organization = models.CharField(max_length=254, null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name


class Campaign(models.Model):

    campaign_name = models.CharField(max_length=254, null=True, blank=True)
    campaign_title = models.CharField(max_length=250, null=True, blank=True)
    templateresource = models.ForeignKey(
        TemplateResource, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=250, null=True, blank=True)
    end_date = models.CharField(max_length=240, blank=True, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    targetusergroup = models.ManyToManyField(
        TargetUserGroup, related_name='campaign')
    target_users_mail_list = models.TextField(blank=True, null=True)
    campaign_opened_count = models.IntegerField(
        default=0, blank=True, null=False)
    hide_camapaign_status = models.BooleanField(default=False)
    campaign_schedule_status = models.BooleanField(default=False)
    start_time = models.CharField(max_length=150 , null=True, blank=True)
    campaign_email_detail_message = models.CharField(max_length=254 , null=True, blank=True)
    camapign_email_title_message = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.campaign_name


class TargetUser(models.Model):

    email = models.EmailField(max_length=254)
    targetusergroup = models.ManyToManyField(
        TargetUserGroup, related_name='targetuser',  blank=True)
    target_user_uuid = models.UUIDField()
    campaign_opened_status = models.BooleanField(default=False)
    email_opened_status = models.BooleanField(default=False)
    opened_campaign_list = models.ManyToManyField(Campaign, blank=True, related_name="opened_campaign")
    associated_campaign_list = models.ManyToManyField(Campaign, blank=True, related_name="associated_campaign")
    password_leaked_status = models.BooleanField(default=False )
    email_credential = models.EmailField(max_length=254, blank=True, null=True)
    password_credential = models.CharField(
        max_length=254, blank=True, null=True, )
    leaked_password_credential = models.CharField(
        max_length=254, blank=True, null=True, )
    user_agent_data = models.TextField(blank=True, null=True)
    browser = models.CharField(
        max_length=254, blank=True, null=True)
    operating_sys =  models.CharField(
        max_length=254, blank=True, null=True, )
    
  

    def __str__(self):
        return self.email


class TargetUserCSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name


class CampaignStatus(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    targetuser = models.ForeignKey(TargetUser, on_delete=models.CASCADE)
    campaign_opened_date = models.DateField(blank=True, null=True )
    
    
    def __str__(self):
        return str(self.campaign_opened_date)
    
    

class UserLogger(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    dateandtime= models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=254, null=True, blank=True)
    action=models.CharField(max_length=254, null=True, blank=True)
    request_url = models.CharField(max_length=254, null= True, blank=True )
    
    def __str__(self):
        return self.user.username