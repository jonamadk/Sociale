from django.contrib import admin
from .models import *
# Register your models here.


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_name', 'templateresource', 'user')


admin.site.register(Campaign, CampaignAdmin)


admin.site.register(TargetUser)


class TargetUserGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'department', 'organization', 'user')


admin.site.register(TargetUserGroup, TargetUserGroupAdmin)


class TargetUserCsvAdmin(admin.ModelAdmin):
    list_display = ('activated', 'file_name')


admin.site.register(TargetUserCSV, TargetUserCsvAdmin)
