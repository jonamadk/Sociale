from django.contrib import admin
from .models import *

models = [Template , TemplateResource]
for model in models:

# Register your models here.

    admin.site.register(model)