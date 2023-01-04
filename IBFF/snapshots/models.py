import uuid
import datetime
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


def update_or_create_snapshots(portfolio):
    today = datetime.date.today()
    try:
        snapshot = Snapshot.objects.get(date__year=today.year)
        snapshot.annual_dividends = portfolio.annual_dividends
        snapshot.annual_gain = portfolio.annual_gain
        snapshot.annual_yield = portfolio.annual_yield
        snapshot.deposit = portfolio.deposit
        snapshot.cash = portfolio.cash
        snapshot.value = portfolio.value
        snapshot.transactions_cost = portfolio.transactions_cost
        snapshot.transactions_counter = portfolio.transactions_counter
        snapshot.save()

    except Snapshot.DoesNotExist:
        Snapshot.objects.create(
            portfolio=portfolio,
            date=today,
            deposit=portfolio.deposit,
            cash=portfolio.cash,
            value=portfolio.value,
            annual_gain=portfolio.annual_gain,
            annual_yield=portfolio.annual_yield,
            annual_dividends=portfolio.annual_dividends,
            transactions_counter=portfolio.transactions_counter,
            transactions_cost=portfolio.transactions_cost
        )
