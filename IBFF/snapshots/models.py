import uuid
from django.db import models
from portfolios.models import Portfolio


class Snapshot(models.Model):
    uusid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=63, unique=True)
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='snapshots'
    )
    date = models.DateTimeField()

    deposit = models.FloatField()
    cash = models.FloatField()
    value = models.FloatField()
    annual_gain = models.FloatField()
    annual_yield = models.FloatField()
    annual_dividends = models.FloatField()
    transactions_cost = models.FloatField()
    transactions_counter = models.IntegerField()

    def __str__(self):
        return self.slug
