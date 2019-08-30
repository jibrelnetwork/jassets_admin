from django.contrib import admin

from .models import TradingPair, Platform, Asset, Exchange


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'main_asset_obj')


class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'name', 'description', 'platform_obj', 'symbol',
                    'type', 'is_active', 'address', 'properties', 'created',
                    'updated')


class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'url')


class TradingPairAdmin(admin.ModelAdmin):
    list_display = ('id', 'base_asset_obj', 'quote_asset_obj', 'exchange_obj',
                    'symbol')


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(TradingPair, TradingPairAdmin)
