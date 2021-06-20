from django.db import models
from user.models import UserModel

# Create your models here.


class Template(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    template_file = models.FileField(blank=True, null=True)
    created_date = models.CharField(blank=True, null=True, max_length=50)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TemplateResource(models.Model):
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
    # template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return self.template_name
