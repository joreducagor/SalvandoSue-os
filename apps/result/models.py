from django.db import models
from django.contrib.auth.models import User

class Result(models.Model):
  tweet = models.TextField(null = True, blank = True)
  owner_screen = models.CharField(max_length = 100, null = True, blank = True)
  owner_name = models.CharField(max_length = 100, null = True, blank = True)
  user = models.ForeignKey(User, null = True, blank = True, on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now = True)

  class Meta:
    verbose_name = "Result"
    verbose_name_plural = "Results"

  def __str__(self):
    return '%s' % (self.tweet)