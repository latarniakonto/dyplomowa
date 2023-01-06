from rest_framework import serializers
from snapshots.models import Snapshot
from portfolios.models import Portfolio


class PortfolioRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        owner = self.context['request'].user
        return Portfolio.objects.filter(owner=owner)


class SnapshotSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    cash_on_hand = serializers.FloatField(source='cash')
    portfolio = PortfolioRelatedField(read_only=True, allow_null=False)

    class Meta:
        model = Snapshot
        exclude = ['id', 'cash']
