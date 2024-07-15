from rest_framework import viewsets

from users.models import UserProfile
from users.serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all()
