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
    
    def update(self, instance, validated_data):
        new_current_price = validated_data.get('current_price')
        instance.current_price = new_current_price
        instance.current_value = instance.current_price * instance.total
        instance.gain = instance.current_value / instance.initial_value - 1
        instance.save()

        assets = Asset.objects.all()
        total_current_value = 0
        for asset in assets:
            total_current_value += asset.current_value
        
        for asset in assets:
            asset.current_weight = asset.current_value / total_current_value
            asset.save()

        return instance
