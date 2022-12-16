from rest_framework import serializers
from transactions.models import Transaction
from portfolios.models import Portfolio


class PortfolioRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        owner = self.context['request'].user
        return Portfolio.objects.filter(owner=owner)


class TransactionSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    portfolio = PortfolioRelatedField(read_only=True, allow_null=False)

    class Meta:
        model = Transaction
        exclude = ['id']
