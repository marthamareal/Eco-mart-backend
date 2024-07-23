from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import IsAdminUser


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
