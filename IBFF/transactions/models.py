import uuid
from django.conf import settings
from django.db import models
from portfolios.models import Portfolio


class Types(models.IntegerChoices):
    BUY = 0, 'Buy'
    SELL = 1, 'Sell'


class Transaction(models.Model):
    uutid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=63, unique=True)
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='transactions'
    )

    ticker = models.CharField(max_length=31)
    type = models.IntegerField(choices=Types.choices, verbose_name='transaction type')
    price = models.FloatField()
    amount = models.IntegerField()
    provision = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.ticker
