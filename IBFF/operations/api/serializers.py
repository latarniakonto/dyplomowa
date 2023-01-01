from rest_framework import serializers
from operations.models import Dividend
from portfolios.models import Portfolio
from assets.models import Asset


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
    asset = AssetRelatedField(allow_null=False)

    class Meta:
        model = Dividend
        exclude = ['id', 'value']
