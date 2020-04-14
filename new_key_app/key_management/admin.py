from django.contrib import admin
from .models import Application, ApplicationKey
from rest_framework_api_key.admin import APIKeyModelAdmin


# Register your models here.
admin.site.register(Application)
@admin.register(ApplicationKey)
class ApplicationKeyAdminSite(APIKeyModelAdmin):
    pass