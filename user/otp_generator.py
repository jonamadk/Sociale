import random


def otp_code_generator():
    '''Function to generate a 6-digit OTP code'''
    otp_code_generate_range = [x for x in range(0, 9)]
    otp_code_list = []
    for tokens in range(0, 6):
        otp_value = random.choice(otp_code_generate_range)
        otp_code_list.append(otp_value)
        otp_code = "".join(str(item) for item in otp_code_list)

    return otp_code
