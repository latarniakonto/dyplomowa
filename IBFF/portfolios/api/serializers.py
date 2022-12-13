from rest_framework import serializers
from portfolios.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    cash_on_hand = serializers.FloatField(source='cash')

    class Meta:
        model = Portfolio
        exclude = ['cash']
