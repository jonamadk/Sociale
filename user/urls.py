from django.urls import path, include


from .views import *

user_crud_patterns = [
    path("update/profile/", UserUpdateView.as_view(), name="user-profile-update"),
    path("delete/", UserDeleteView.as_view(), name="user-deletion"),
    path("view/", UserRetrieveView.as_view()),
    path("update/password/", UserProfilePasswordUpdateView.as_view(), name="user-password-update"),
    path("state/", CheckUserState.as_view()),
    path('log/', UserLogAPI.as_view())

]


urlpatterns = [

    path("signup/", UserSignupView.as_view(), name="user-signup"),
    path("signin/", UserSiginView.as_view(), name='user-signin'),
    path("signin/2f/", TwoFactorCheckandRoute.as_view(), name="check-auth-type"),
    path("users/", UserListView.as_view()),
    path("user/", include(user_crud_patterns)),
    path("email/", ForgetPasswordView.as_view(), name="forgot-password"),
    path("verify/otp/", OTPVerifyView.as_view(), name="user-otp-verify"),
    path("disable/twofactor/", DisableTwoFactorAuthView.as_view()),
    path("select/twofactor/", SelectTwoFactorAuthView.as_view()),
    path("status/auth/", UserAuthStatusView.as_view()),
    path("check/", SendOTPInMailView.as_view(), name="send-otp-mail"),  
    path("pnumber/", GetPhoneNumberFromEmailView.as_view()),
    path("mail/", OTPSendInUserEmail.as_view()),
    path("verify/", OTPVerifyForForgetPassword.as_view(), name="otp-verify-forgot-password"),
    path("setpassword/", AddNewPassword.as_view(), name ="user-new-password")

]
