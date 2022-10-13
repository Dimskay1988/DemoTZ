from apps.Base.views import CatalogView, DataView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()

urlpatterns = [

    path('catalog/', DataView.as_view()),

]

router.register(r'product', CatalogView, basename='products')

urlpatterns += router.urls
