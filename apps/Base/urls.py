from apps.Base.views import CatalogView, ArticleView
from rest_framework.routers import DefaultRouter
from django.urls import path

# router = DefaultRouter()

urlpatterns = [

    path('input/', ArticleView.as_view()),
    path('product/', CatalogView.as_view({'get': 'list'})),

]

# router.register(r'product', CatalogView, basename='products')

# urlpatterns += router.urls
