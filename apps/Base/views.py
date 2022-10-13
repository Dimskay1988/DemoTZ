from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from apps.Base.models import Catalog
from rest_framework import status
from rest_framework.response import Response
from apps.Base.serializers import CatalogSerializer, NewArticleSerializer
import requests


class CatalogView(viewsets.ModelViewSet):
    """
    Product from the catalog
    """
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()


class ArticleView(generics.GenericAPIView):
    serializer_class = NewArticleSerializer

    def post(self, request):
        article = request.data.get('article')
        req = requests.get(f'https://basket-05.wb.ru/vol735/part73512/{article}/info/ru/card.json').json()
        data = {
            'article': req.get('nm_id'),
            'brand': req.get('selling').get('brand_name'),
            'title': req.get('description')
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return Response({'article': NewArticleSerializer(article, context=self.get_serializer_context()).data})
