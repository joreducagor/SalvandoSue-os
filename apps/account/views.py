from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.account.serializers import LinkedAccountSerializer
from apps.account.models import LinkedAccount
from apps.user.models import User
import json

class APILinkedAccountList(APIView):

	def get(self, request, format=None):
		linked_accounts = LinkedAccount.objects.all()
		linked_account_json = LinkedAccountSerializer(linked_accounts, many = True)
		return Response({'linked_accounts': linked_account_json.data})

	def post(self, request):
		try:
			user = User.objects.get(username = request.data['username'])
		except User.DoesNotExist:
			user = None
		try:
			linked_account = LinkedAccount.objects.filter(twitter_user_id = request.data['linked_account_params']['twitter_user_id']).first()
		except LinkedAccount.DoesNotExist:
			linked_account = None
		if user is not None:
			if linked_account is not None:
				linked_account.users.add(user)
				return Response({"success": True}, status = 200)
			else:
				linked_account_json = LinkedAccountSerializer(data = request.data['linked_account_params'])
				if linked_account_json.is_valid():
					linked_account = linked_account_json.save()
					linked_account.users.add(user)
					return Response(linked_account_json.data, status = 201)
				return Response(linked_account_json.errors, status = 400)
		else:
			return Response({"user": "invalid username"})

	def delete(self, request):
		try:
			user = User.objects.get(username = request.data['username'])
		except User.DoesNotExist:
			user = None
		if user is not None:
			try:
				linked_account = LinkedAccount.objects.get(twitter_user_id = request.data['twitter_user_id'])
			except LinkedAccount.DoesNotExist:
				linked_account = None
			if linked_account is not None:
				linked_account.users.remove(user)
				return Response({"success": True}, status = 200)
			else:
				return Response({"success": False}, status = 200)
		else:
			return Response({"user": "invalid username"})



class APIVerifyLinkedAccount(APIView):

	def post(self, request):
		try:
			user = User.objects.get(username = request.data['username'])
		except User.DoesNotExist:
			user = None
		if user is not None:
			linked_accounts = user.linkedaccount_set.all()
			try:
				linked_account = linked_accounts.get(twitter_user_id = request.data['twitter_user_id'])
			except LinkedAccount.DoesNotExist:
				linked_account = None
			if linked_account is not None:
				return Response({"linked_account": True})
			else:
				return Response({"linked_account": False})
		else:
			return Response({"user": "invalid username"})