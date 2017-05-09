from rest_framework.serializers import ModelSerializer
from apps.account.models import LinkedAccount

class LinkedAccountSerializer(ModelSerializer):
	
	class Meta:
		model = LinkedAccount
		fields = ('id', 'twitter_user_id', 'twitter_token', 'created_at')