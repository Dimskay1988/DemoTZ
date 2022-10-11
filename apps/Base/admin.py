from django.contrib import admin
from apps.Base.models import Catalog


@admin.register(Catalog)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('article', 'brand', 'title')
    fields = ['id', 'article', 'brand', 'title']
    search_fields = ['article', 'brand']
