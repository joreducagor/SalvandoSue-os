from django.conf.urls import url, include
from apps.account.views import APILinkedAccountList

urlpatterns = [
	url(r'^linked_accounts/$', APILinkedAccountList.as_view(), name="APILinkedAccountList"),
]
