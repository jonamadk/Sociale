
from django.db import models
from template.models import TemplateResource
from user.models import UserModel
# Create your models here.





class TargetUserGroup(models.Model):

    group_name = models.CharField(max_length = 254 , null = True , blank = True)
    department = models.CharField(max_length = 254 , null = True , blank = True)
    organization = models.CharField(max_length = 254 , null = True , blank = True)
    user = models.ForeignKey(UserModel,on_delete = models.CASCADE )


    def __str__(self):
        return self.group_name
    

class Campaign(models.Model):

    campaign_name = models.CharField(max_length = 254, null = True, blank= True)
    campaign_title = models.CharField(max_length = 250 , null = True , blank = True)
    templateresource = models.ForeignKey(TemplateResource, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=250, null = True, blank = True)
    end_date = models.CharField(max_length=240, blank=True, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    targetusergroup = models.ManyToManyField(TargetUserGroup, related_name='campaign')
    target_users_mail_list = models.TextField(blank=True, null=True)
    campaign_opened_count =models.IntegerField(default=0 , blank=True, null=False)
    hide_camapaign_status = models.BooleanField(default=False)
    campaign_schedule_status = models.BooleanField(default=False)

    def __str__(self):
        return self.campaign_name



class TargetUser(models.Model):

    email = models.EmailField(max_length=254, unique=True)
    targetusergroup = models.ManyToManyField(TargetUserGroup ,related_name = 'targetuser',  blank=True)
    target_user_uuid = models.UUIDField(blank=True , null = True)
    status = models.BooleanField(default =False)
    opened_campaign_list = models.ManyToManyField(Campaign,blank = True)
    email_credential= models.EmailField(max_length=254, blank = True , null = True)
    password_credential = models.CharField(max_length=254, blank=True , null=True, )
    leaked_password_credential =models.CharField(max_length=254, blank=True , null=True, )
  


    
    
    def __str__(self):
        return self.email





class TargetUserCSV(models.Model):
    file_name = models.FileField(upload_to = 'csvs')
    uploaded = models.DateTimeField(auto_now_add = True)
    activated = models.BooleanField(default = False)


    def _str__(self):
        return self.file_name

