from rest_framework import viewsets
from rest_framework.views import APIView
from apps.Base.models import Catalog
from rest_framework import status
from rest_framework.response import Response
from apps.Base.serializers import CatalogSerializer
import json
import requests


class CatalogView(viewsets.ModelViewSet):
    """
    Product from the catalog
    """
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()


class DataView(APIView):
    def get(self, request):
        req = requests.get('https://basket-05.wb.ru/vol735/part73512/73512949/info/ru/card.json').json()
        data = {
            'article': req.get('nm_id'),
            'brand': req.get('imt_name'),
            'title': req.get('description')
        }
        return Response(data, status=status.HTTP_200_OK)

