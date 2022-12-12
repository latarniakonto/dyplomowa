import uuid
from django.conf import settings
from django.db import models


class Portfolio(models.Model):
    uupid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=63, unique=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portfolios'
    )

    name = models.CharField(max_length=31)
    deposit = models.FloatField()
    cash = models.FloatField()
    value = models.FloatField()
    annual_gain = models.FloatField()
    annual_yield = models.FloatField()
    annual_dividends = models.FloatField()
    transactions_cost = models.FloatField()
    transactions_counter = models.IntegerField()

    def __str__(self):
        return self.name
