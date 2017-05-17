from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.serializers import UserSerializer, DetailUserSerializer
from apps.account.serializers import LinkedAccountSerializer
import json

class APIUserList(APIView):
	
	def get(self, request, format = None):
		users = User.objects.all()
		users_json = UserSerializer(users, many = True)
		return Response({'users': users_json.data})

	def post(self, request):
		user_json = UserSerializer(data = request.data)
		if user_json.is_valid():
			user_json.save()
			return Response(user_json.data, status = 201)
		else:
			try:
				found_user = User.objects.get(username = request.data["username"])
			except User.DoesNotExist:
				found_user = None
			if found_user is not None:
				found_user_json = UserSerializer(found_user)
				return Response(found_user_json.data, status = 200)
		return Response(user_json.errors, status = 400)

class APIUserDetail(APIView):

	def set_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		user = self.set_object(pk)
		user_json = UserSerializer(user)
		return Response(user_json.data)

	def put(self, request, pk):
		user = self.set_object(pk)
		user_json = UserSerializer(user, data = request.data)
		if user_json.is_valid():
			user_json.save()
			return Response(user_json.data)
		return Response(user_json.data, status = 400)

class APIUserLinkedAccounts(APIView):

	def set_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		user = self.set_object(pk)
		linked_accounts = user.linkedaccount_set.all()
		linked_accounts_json = LinkedAccountSerializer(linked_accounts, many = True)
		return Response({"linked_accounts": linked_accounts_json.data})