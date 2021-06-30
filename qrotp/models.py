from django.db import models
from user.models import UserModel
# Create your models here.


class MFHash(models.Model):
    mfa_hash = models.CharField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
