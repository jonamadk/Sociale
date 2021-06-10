from django import template
from django.urls import path , include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

campaign = [
    path('create/' , CreateCampaignView.as_view()),
    path('update/', UpdateCampaignView.as_view()),
    path('getlist/', RetrieveCampaignListView.as_view()),
    path('hide/', HideCampaignView.as_view()),
    path('retrieve/', RetrieveCampaignView.as_view()),
    path('target_mail_list/', AddTemplateReceiverList.as_view()),
    path("send/", SendTemplateMailView.as_view()),
    path("schedule", ScheduleCamapaignView.as_view()),
    path('send/image_load/<str:targetuser_uuid>/<int:camp_id>/',image_load, name='image_load'),
    # path('email_opened_status/<str:targetuser_uuid>/<int:camp_id>/',GetTargetUserAffiliatedCampaign.as_view()),
    path('check/', CheckPawnPassword.as_view()),
    # path('send/template_resource/<str:targetuser_uuid>/<str:temp_resource>/',template_load, name='template_resource'),
    path('ua_data/', GetUserAgentData.as_view()),
    path('check/targetuser_leak/', TargetUserCredentials.as_view()),
    path('validate/template/', ValidateTemplate.as_view())
]


group = [
    path('create/', CreateTargetUserGroupView.as_view()),
    path('get/', GetTargetUserGroupListView.as_view()),
    path('update/', UpdateTargetUserGroupView.as_view()),
    path('delete/', DeleteTargetUserListView.as_view()),
    path('list/', GetTargetUserGroupFromOrganizationView.as_view())

]




targetuser = [
    path('create/', AddTargetUserEmailView.as_view()),
    path('dump/', CSVUploadView.as_view()),
    path('get/', GetTargetUserListView.as_view()),
    path('update/', UpdateTargetUserListView.as_view()),
]

urlpatterns = [
    path('targetusergroup/', include(group)),
    path('targetuser/', include(targetuser)),
    path('campaign/', include(campaign))
] 
