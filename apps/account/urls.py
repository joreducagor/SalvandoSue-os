from django.conf.urls import url, include
from apps.account.views import APILinkedAccountList, APIVerifyLinkedAccount

urlpatterns = [
  url(r'^linked_accounts/$', APILinkedAccountList.as_view(), name="APILinkedAccountList"),
  url(r'^linked_accounts/verify/$', APIVerifyLinkedAccount.as_view(), name="APIVerifyLinkedAccount"),
]
