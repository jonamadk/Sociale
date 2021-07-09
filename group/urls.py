from django.urls import path, include
from .views import *


extra_patterns = [

    path('create/', UsersGroupCreateView.as_view()),
    path('get/', GetUserGroupList.as_view()),
    path('permissions/', GetPermissionsList.as_view()),
    path('update/', GroupUpdateView.as_view()),
    path('delete/', GroupDeleteView.as_view()),
    path('perm/', AdjustedPermissions.as_view()),
    path('testmail/', TestEmail.as_view()),
    path('details/', GetUserGroupandPermissions.as_view()),
    path('viewpermissions/', GetPermissionsFromGroup.as_view()),


]


urlpatterns = [

    path('group/', include(extra_patterns)),

]
