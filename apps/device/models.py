from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
	DEVICES_TYPES = (
    ('0', 'android'),
    ('1', 'ios'),
	)
	device_type = models.CharField(max_length = 1, choices = DEVICES_TYPES)
	uuid = models.TextField(blank=True, null=True)
	key = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name = "Device"
		verbose_name_plural = "Devices"

	def __str__(self):
		return '%s %s' % (self.device_type, self.uuid)