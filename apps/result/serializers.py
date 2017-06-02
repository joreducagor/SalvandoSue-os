from rest_framework.serializers import ModelSerializer
from apps.result.models import Result

class ResultSerializer(ModelSerializer):
  class Meta:
    model = Result
    fields = ('tweet', 'owner_screen', 'owner_name', 'created_at')