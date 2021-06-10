from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth.models import Permission


class GroupSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = Group
        fields = ('id','name','permissions',)

class PermissionSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = Permission
        fields = ('codename','id','name','content_type')