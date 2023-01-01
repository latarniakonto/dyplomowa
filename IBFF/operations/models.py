import uuid
from django.db import models
from assets.models import Asset
from core.utils import future_date
from datetime import datetime
from core.utils import get_asset_to_date


class Operation(models.Model):
    uuoid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=63, unique=True)
    date = models.DateTimeField()

    class Meta:
        abstract = True


class Dividend(Operation):
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, related_name='dividends'
    )
    per_share = models.FloatField()
    value = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if 'normal_save' in kwargs:
            super().save(args, kwargs)
            return

        if future_date(self.date):
            raise Exception
        
        to_date_asset = get_asset_to_date(self.asset, self.date)
        if to_date_asset.total == 0:
            raise Exception

        self.value = to_date_asset.total * self.per_share        
        
        portfolio = self.asset.portfolio
        portfolio.cash += self.value
        portfolio.value += self.value
        portfolio.annual_dividends += self.value
        portfolio.annual_gain = portfolio.value - portfolio.deposit
        portfolio.annual_yield = portfolio.value / portfolio.deposit - 1
        portfolio.save()

        # update snapshots???

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.asset.portfolio.cash < self.value:
            raise Exception

        portfolio = self.asset.portfolio
        portfolio.cash -= self.value
        portfolio.value -= self.value
        portfolio.annual_dividends -= self.value
        portfolio.annual_gain = portfolio.value - portfolio.deposit
        portfolio.annual_yield = portfolio.value / portfolio.deposit - 1
        portfolio.save()

        # update snapshots???
        super().delete(*args, **kwargs)
