from rest_framework import serializers
from assets.models import Asset
from portfolios.models import Portfolio


class PortfolioRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        owner = self.context['request'].user
        return Portfolio.objects.filter(owner=owner)


class AssetSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    portfolio = PortfolioRelatedField(read_only=True, allow_null=False)

    class Meta:
        model = Asset
        exclude = ['id']
