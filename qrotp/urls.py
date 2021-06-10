from django.urls import path , include 
from .views import *




urlpatterns = [

    path('enable/totp/', EnableQRBasedTOTP.as_view()),
    path('signin/totp/' , TOTPVerifyView.as_view())
]
