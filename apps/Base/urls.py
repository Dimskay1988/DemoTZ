from apps.Base.views import CatalogView, DataView, ArticleView
from rest_framework.routers import DefaultRouter
from django.urls import path

# router = DefaultRouter()

urlpatterns = [

    path('catalog/', DataView.as_view()),
    path('input/', ArticleView.as_view()),
    path('product/', CatalogView.as_view({'get': 'list'})),

]

# router.register(r'product', CatalogView, basename='products')

# urlpatterns += router.urls
