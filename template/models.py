from django.db import models
from user.models import UserModel

# Create your models here.




class TemplateResource(models.Model):
    '''Model to store template resource information'''
    headerBackgroundColor = models.CharField(
        max_length=100, blank=True, null=True)
    headerFontColor = models.CharField(max_length=100, blank=True, null=True)
    headerNav1 = models.CharField(max_length=100, blank=True, null=True)
    headerNav2 = models.CharField(max_length=100, blank=True, null=True)
    headerNav3 = models.CharField(max_length=100, blank=True, null=True)
    bodyBackgroundcolor = models.CharField(
        max_length=100, null=True, blank=True)
    bodyFontColor = models.CharField(max_length=100, blank=True, null=True)
    bodyButtonColor = models.CharField(max_length=120, null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    template_name = models.CharField(
        max_length=250, blank=True, null=True, unique=True)
    template_url = models.CharField(max_length=250, blank=True, null=True)


    def __str__(self):
        return self.template_name
