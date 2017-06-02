from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.result.serializers import ResultSerializer
from apps.result.models import Result
import json

class APIResultList(APIView):
  
  def get(self, request, format = None):
    results = Result.objects.all()
    results_json = ResultSerializer(results, many = True)
    return Response({'results': results_json.data})