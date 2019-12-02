from rest_framework import serializers
from profile_api import models


class HelloSerializers(serializers.Serializer):
    """serialize name field for testing our api """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serial a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ Create and return a new user """
        user = models.UserProfile.objects.create_superuser(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
