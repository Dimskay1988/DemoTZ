from apps.Base.views import CatalogView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'product', CatalogView, basename='products')

urlpatterns = router.urls
