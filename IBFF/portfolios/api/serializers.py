import datetime
from rest_framework import serializers
from portfolios.models import Portfolio
from users.models import IBFFUser
from snapshots.models import Snapshot


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

        today = datetime.date.today()
        try:
            snapshot = Snapshot.objects.get(
                portfolio=instance, date__year=today.year - 1
            )
            instance.annual_gain = instance.value - snapshot.value
            instance.annual_yield = instance.value / snapshot.value - 1

        except Snapshot.DoesNotExist:
            instance.annual_gain = instance.value - instance.deposit
            instance.annual_yield = instance.value / instance.deposit - 1
        
        instance.save()
        return instance 
