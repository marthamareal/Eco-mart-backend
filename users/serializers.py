from rest_framework import serializers

from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_superuser')
        read_only_fields = ['is_superuser']

        extra_kwargs = {
            'password': {'write_only': True}
        }
