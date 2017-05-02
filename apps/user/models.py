from django.db import models
from django.contrib.auth.models import User

class DetailUser(models.Model):
	twitter_token = models.CharField(max_length=50)
	dob = models.DateField()
	phone = models.CharField(max_length=9)
	enabled = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "DetailUser"
		verbose_name_plural = "DetailUsers"

	def __str__(self):
		return '%s %s' % (self.user.first_name, self.user.last_name)

class Device(models.Model):
	DEVICES_TYPES = (
    ('0', 'android'),
    ('1', 'ios'),
	)
	device_type = models.CharField(max_length=1, choices=DEVICES_TYPES)
	uuid = models.CharField(max_length=50)
	key = models.CharField(max_length=50)
	user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Device"
		verbose_name_plural = "Devices"

	def __str__(self):
		return '%s %s' % (self.device_type, self.uuid)

class Session(models.Model):
	access_token = models.CharField(max_length=50)
	refresh_token = models.CharField(max_length=50)
	key = models.CharField(max_length=50)
	expires_at = models.DateField()
	device = models.OneToOneField(Device, null=False, blank=False, on_delete=models.CASCADE)
	user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Session"
		verbose_name_plural = "Sessions"

	def __str__(self):
		return self.access_token