from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from apps.user.models import DetailUser

class DetailUserSerializer(ModelSerializer):
	class Meta:
		model = DetailUser
		fields = ('twitter_token', 'dob', 'phone', 'enabled', 'created_at')

class UserSerializer(ModelSerializer):
  detailuser = DetailUserSerializer()

  class Meta:
  	model = User
  	fields = ('id', 'username', 'first_name', 'last_name', 'email', 'detailuser')

  def create(self, validated_data):
    detailuser = validated_data.pop('detailuser')
    user = User.objects.create(**validated_data)
    DetailUser.objects.create(user=user, **detailuser)
    return user