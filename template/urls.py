from django.urls import path, include
from .views import *





resource_patterns = [
    path("create/", CreateResourceView.as_view()),
    path("update/", UpdateTemplateResourceView.as_view()),
    path("list/", TemplateResourceListView.as_view()),
    path("retrieve", TemplateResourceRetrieveView.as_view()),
    path('get/', AllTemplateResourceListView.as_view()),
    path('delete/', DeleteTemplateResourceView.as_view())
]

urlpatterns = [
    path("template/resource/", include(resource_patterns)),

]
