from django.conf.urls import url, include
from apps.device.views import APIDeviceList

urlpatterns = [
	url(r'^devices/$', APIDeviceList.as_view(), name="APIDeviceList"),
]
