from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator


class UploadSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[UniqueValidator(
        Template.objects.all())], max_length=None, required=True)

    class Meta:
        model = Template
        fields = ['template_file', 'name']


class GetTemplateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[UniqueValidator(
        Template.objects.all())], max_length=None, required=True)

    class Meta:
        model = Template
        fields = ['template_file', 'name', 'id']


class TemplateResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = TemplateResource
        fields = '__all__'


class TemplateResourceUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = TemplateResource
        fields = ['headerBackgroundColor', 'headerFontColor', 'headerNav1', 'headerNav2', 'headerNav3',
                  'bodyBackgroundcolor', 'bodyFontColor', 'bodyButtonColor', 'template_name', 'template_url']
