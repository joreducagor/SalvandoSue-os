from django.conf.urls import url, include
from apps.account.views import APILinkedAccountList, APIVerifyLinkedAccount, APILinkedAccountTweets

urlpatterns = [
  url(r'^linked_accounts/$', APILinkedAccountList.as_view(), name="APILinkedAccountList"),
  url(r'^linked_accounts/verify/$', APIVerifyLinkedAccount.as_view(), name="APIVerifyLinkedAccount"),
  url(r'^linked_accounts/(?P<pk>[0-9]+)/tweets/$', APILinkedAccountTweets.as_view(), name="APILinkedAccountTweets"),
]
