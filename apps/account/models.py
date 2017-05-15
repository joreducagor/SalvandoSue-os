from django.db import models
from apps.user.models import User

class LinkedAccount(models.Model):
  twitter_user_id = models.CharField(max_length = 50)
  twitter_token = models.CharField(max_length = 50, null = True, blank = True)
  twitter_screen_name = models.CharField(max_length = 50, null = True, blank = True)
  created_at = models.DateTimeField(auto_now = True)
  users = models.ManyToManyField(User)

  class Meta:
    verbose_name = "Account"
    verbose_name_plural = "Accounts"

  def __str__(self):
    return (self.twitter_user_id)