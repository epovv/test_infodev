from django.contrib import admin
from alert.models import *

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    """Описание модели Device в админке"""

    list_display = ('id', 'type', 'activity', 'address')
    list_filter = ('type', 'activity')

admin.site.register(Device, DeviceAdmin)