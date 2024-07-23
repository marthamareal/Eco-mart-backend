"""
URL configuration for Ecomart project.
"""

from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


# swagger settings
schema_view = get_schema_view(
   openapi.Info(
      title="EcoMart APIs",
      default_version='v0.0.0',
      description="Welcome to the API Documentation",
   ),
   public=True,
   permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("", include("users.urls")),
    path("", include("products.urls")),
]
