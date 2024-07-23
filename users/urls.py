from rest_framework import routers

from users.views import UserProfileViewSet

router = routers.SimpleRouter()
router.register("users", UserProfileViewSet, basename="users")

urlpatterns = router.urls
