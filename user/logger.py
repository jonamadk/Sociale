
from rest_framework.reverse import reverse
from django.http import request
from datetime import datetime
from campaign.models import UserLogger




def logger_is(request ,message,action, url_name):
    url_data = {
            'url': reverse(url_name, request=request)
        }
    time_now = datetime.now()
    userlog = UserLogger.objects.create(user = request.user, message=message, action =action, request_url = url_data['url'])
    return True
    