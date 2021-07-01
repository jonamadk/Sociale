from django.urls import path, include


from .views import *

user_crud_patterns = [
    path("update/profile/", UserUpdateView.as_view()),
    path("<int:pk>/delete/", UserDeleteView.as_view()),
    path("view/", UserRetrieveView.as_view()),
    path("update/password/", UserProfilePasswordUpdateView.as_view()),
    path("state/", CheckUserState.as_view())

]


urlpatterns = [

    path("signup/", UserSignupView.as_view()),
    path("signin/", UserSiginView.as_view()),
    path("signin/2f/", TwoFactorCheckandRoute.as_view()),
    path("users/", UserListView.as_view()),
    path("user/", include(user_crud_patterns)),
    path("setpassword/", ForgetPasswordView.as_view()),
    path("verify/otp/", OTPVerifyView.as_view()),
    path("disable/twofactor/", DisableTwoFactorAuthView.as_view()),
    path("select/twofactor/", SelectTwoFactorAuthView.as_view()),
    path("status/auth/", UserAuthStatusView.as_view()),
    path("check/", SendOTPInMailView.as_view()),
    path("pnumber/", GetPhoneNumberFromEmailView.as_view()),
    path("mail/", OTPSendInUserEmail.as_view())


]
