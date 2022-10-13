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
            'article',
        ]

    def create(self, validated_data):
        article = validated_data['article']
        article = Catalog(article=article)
        article.save()
        return article
