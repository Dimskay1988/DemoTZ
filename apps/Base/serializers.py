from rest_framework import serializers
from .models import Catalog


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class NewArticleSerializer(serializers.ModelSerializer):
    article = serializers.IntegerField(write_only=True, style={'input_type': 'article'})

    class Meta:
        model = Catalog
        fields = [
            'article', 'brand', 'title'
        ]

    def create(self, validated_data):
        article = validated_data['article']
        brand = validated_data['brand']
        title = validated_data['title']
        data = Catalog(article=article, brand=brand, title=title)
        data.save()
        return data
