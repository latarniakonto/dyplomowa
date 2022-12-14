from rest_framework import serializers
from portfolios.models import Portfolio
from users.models import IBFFUser


class UserRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        return IBFFUser.objects.filter(username=user)


class PortfolioSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    cash_on_hand = serializers.FloatField(source='cash')
    owner = UserRelatedField(required=True, allow_null=False)

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
