from django import template
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings



##### Campaign URLs
campaign = [
    path('create/', CreateCampaignView.as_view()),
    path('update/', UpdateCampaignView.as_view()),
    path('getlist/', RetrieveCampaignListView.as_view()),
    path('hide/', HideCampaignView.as_view()),
    path('retrieve/', RetrieveCampaignView.as_view()),
    path('target_mail_list/', AddTemplateReceiverList.as_view()),
    path("send/", SendTemplateMailView.as_view()),
    path("schedule/", ScheduleCamapaignView.as_view()),
    path('send/image_load/<str:targetuser_uuid>/<int:camp_id>/',
         image_load, name='image_load'),
    path('ua_data/', GetUserAgentData.as_view()),
    path('check/targetuser_leak/', TargetUserCredentials.as_view()),
    path('validate/template/', ValidateTemplate.as_view()),
    path("update/detail/", UpdateCampaignDetailView.as_view()),
    path("update/mail_list/", UpdateCampaignMailListView.as_view()),
    path("list/", RetrieveAllCampaignsFromOrganization.as_view()),
    path("delete/", DeleteCamapaignView.as_view()),
    path("tor-test-one/", TestForTorOne.as_view()),



]

##### Target User Group URLs
group = [
    path('create/', CreateTargetUserGroupView.as_view()),
    path('get/', GetTargetUserGroupListView.as_view()),
    path('update/', UpdateTargetUserGroupView.as_view()),
    path('delete/', DeleteTargetUserGroupView.as_view()),
    path('list/', GetTargetUserGroupFromOrganizationView.as_view()),
    path('all/', GetTargetUserGroupAllView.as_view())

]

###### Target User URLs`
targetuser = [
    path('create/', AddTargetUserEmailView.as_view()),
    path('dump/', CSVUploadView.as_view()),
    path('get/', GetTargetUserListView.as_view()),
    path('update/', UpdateTargetUserListView.as_view()),
]

##### URL Patterns
urlpatterns = [
    path('targetusergroup/', include(group)),
    path('targetuser/', include(targetuser)),
    path('campaign/', include(campaign))
]
