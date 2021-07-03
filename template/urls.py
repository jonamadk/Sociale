from django.urls import path, include
from .views import *


extra_patterns = [
    path("upload/", TemplateUpload.as_view()),
    path("view/", TemplateRetrieveView.as_view()),
    path("delete/", TemplateDeleteView.as_view()),
    path("update/", TemplateUpdateView.as_view()),

]


resource_patterns = [
    path("create/", CreateResourceView.as_view()),
    path("update/", UpdateTemplateResourceView.as_view()),
    path("list/", TemplateResourceListView.as_view()),
    path("retrieve", TemplateResourceRetrieveView.as_view()),
    path('get/', AllTemplateResourceListView.as_view())
]

urlpatterns = [
    path("template/", include(extra_patterns)),
    path("template/resource/", include(resource_patterns)),

]
