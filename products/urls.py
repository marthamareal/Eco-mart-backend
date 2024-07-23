from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet

router = routers.SimpleRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("products", ProductViewSet, basename="products")

urlpatterns = router.urls
