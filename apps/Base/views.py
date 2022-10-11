from rest_framework import viewsets
from apps.Base.models import Catalog
from apps.Base.serializers import CatalogSerializer


class CatalogView(viewsets.ModelViewSet):
    """
    Product from the catalog
    """
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()
