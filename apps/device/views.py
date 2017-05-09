from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.device.serializers import DeviceSerializer, DeviceCreateSerializer
from apps.user.serializers import UserSerializer
from apps.device.models import Device
from apps.user.models import User
import json

class APIDeviceList(APIView):

	def get(self, request, format=None):
		devices = Device.objects.all()
		devices_json = DeviceSerializer(devices, many = True)
		return Response({'devices': devices_json.data})

	def post(self, request):
		try:
			user = User.objects.get(username = request.data['username'])
		except User.DoesNotExist:
			user = None
		if user is not None:
			device_json = DeviceCreateSerializer(data = request.data['device_params'])
			if device_json.is_valid():
				device_json.save(user = user)
				return Response(device_json.data, status = 201)
			return Response(device_json.errors, status = 400)
		else:
			return Response({"user": "invalid username"})