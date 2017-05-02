from django.contrib import admin
from apps.user.models import DetailUser
from apps.user.models import Device
from apps.user.models import Session

admin.site.register(DetailUser)
admin.site.register(Device)
admin.site.register(Session)