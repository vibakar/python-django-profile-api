from rest_framework import serializers
from profiles import models


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ["email", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            }
        }
    
    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeed
        fields = ["id", "user_profile", "status_text", "created_on"]
        extra_kwargs = {
            "user_profile": {
                "read_only": True
            }
        }