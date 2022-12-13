from rest_framework import serializers
from portfolios.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    cash_on_hand = serializers.FloatField(source='cash')

    class Meta:
        model = Portfolio
        exclude = ['cash']

    def update(self, instance, validated_data):
        addend = validated_data.get('deposit') - instance.deposit
        instance.deposit += addend
        instance.cash += addend
        instance.value += addend
        instance.save()

        return instance 
