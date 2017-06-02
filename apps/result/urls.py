from django.conf.urls import url
from apps.result.views import APIResultList

urlpatterns = [
  url(r'^results/$', APIResultList.as_view(), name="APIResultList"),
]
