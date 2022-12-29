import uuid
from django.db import models
from portfolios.models import Portfolio


class Asset(models.Model):
    uuaid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=63, unique=True)
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='assets'
    )

    ticker = models.CharField(max_length=31)
    total = models.IntegerField(default=0)
    initial_price = models.FloatField(default=0)
    current_price = models.FloatField(default=0)
    gain = models.FloatField(default=0)
    current_value = models.FloatField(default=0)
    initial_value = models.FloatField(default=0)
    initial_weight = models.FloatField(default=0)
    current_weight = models.FloatField(default=0)

    def __str__(self):
        return self.ticker
