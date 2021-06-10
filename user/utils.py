from twilio.rest import Client
from decouple import config


account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_sms(otp_code , phonenumber):
     # ADD TWILLIO SMS FACILITY FOR TWO FACTOR AUTHENTICATION
    sms_message = " Your OTP code is : {} .  Please Enter the code for verification ".format(otp_code)

    message = client.messages.create(
        body= sms_message,
        from_ = config("SENDER_PHONENUMBER"),
        to = f'{phonenumber}'
    )