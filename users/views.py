from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsOwnerOrAdmin, IsAdminUser


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        elif self.action == "list":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsOwnerOrAdmin]

        return [permission() for permission in permission_classes]
