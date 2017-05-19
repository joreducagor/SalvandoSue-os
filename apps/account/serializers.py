from rest_framework.serializers import ModelSerializer
from apps.account.models import LinkedAccount

class LinkedAccountSerializer(ModelSerializer):
	
	class Meta:
		model = LinkedAccount
		fields = ('id', 'twitter_user_id', 'twitter_user_name', 'twitter_screen_name', 'twitter_image_url', 'created_at')