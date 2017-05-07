from apps.device.models import Device
from apps.user.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer

class DeviceSerializer(ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Device
		fields = ('device_type', 'uuid', 'key', 'created_at', 'user')

class DeviceCreateSerializer(ModelSerializer):
	class Meta:
		model = Device
		fields = ('device_type', 'uuid', 'key', 'created_at')