from django.urls import path, include
from .views import *


extra_patterns = [

    path('create/', UsersGroupCreateView.as_view()),
    path('get/', GetUserGroupList.as_view()),
    path('permissions/', GetPermissionsList.as_view()),
    path('<int:pk>/update/', GroupUpdateView.as_view()),
    path('<int:pk>/delete/', GroupDeleteView.as_view()),
    path('perm/', AdjustedPermissions.as_view())

]


urlpatterns = [

    path('group/', include(extra_patterns)),

]
