from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class UserModel(AbstractUser):
    '''Custom User Model extending AbstractUser'''
    phonenumber = PhoneNumberField(unique=True)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    email_two_factor_auth = models.BooleanField(
        default=False, null=True, blank=True)
    totp_two_factor_auth = models.BooleanField(
        default=False, null=True, blank=True)
    email_and_sms_two_factor_auth = models.BooleanField(
        default=False, null=True, blank=True)
    
    
    def __str__(self):
        return self.username




   
    
    
    

        


