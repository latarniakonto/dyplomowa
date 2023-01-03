from rest_framework import serializers
from operations.models import Dividend, Types
from portfolios.models import Portfolio
from assets.models import Asset
from assets.api.serializers import AssetSerializer


class AssetRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        user_portfolios = Portfolio.objects.filter(owner=user)

        queryset = Asset.objects.none()
        for portfolio in user_portfolios:
            queryset |= portfolio.assets.all()
        
        return queryset


class DividendSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    asset = AssetSerializer(AssetRelatedField(allow_null=False))    

    class Meta:
        model = Dividend
        exclude = ['id', 'value', 'type']
        depth = 1

    def create(self, validated_data):        
        asset_data = validated_data.pop('asset')
        asset = Asset.objects.get(slug=asset_data['slug'])
        dividend = Dividend.objects.create(
            **validated_data, asset=asset, type=Types.DIVIDEND
        )        
        return dividend
