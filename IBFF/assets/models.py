import uuid
from django.db import models
from portfolios.models import Portfolio
from django.db.models import Q
from transactions.models import Types


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


def get_asset_initial_weight(asset):
    portfolio_assets = Asset.objects.filter(
        ~Q(uuaid=asset.uuaid), portfolio=asset.portfolio
    )
    if len(portfolio_assets) == 0:
        return 1
    
    total_value = asset.initial_value
    for portfolio_asset in portfolio_assets:
        total_value += portfolio_asset.initial_value

    if total_value == 0:
        return 0

    return asset.initial_value / total_value


def get_asset_current_weight(asset):
    portfolio_assets = Asset.objects.filter(
        ~Q(uuaid=asset.uuaid), portfolio=asset.portfolio
    )
    if len(portfolio_assets) == 0:
        return 1

    total_value = asset.current_value
    for portfolio_asset in portfolio_assets:
        total_value += portfolio_asset.current_value
    
    if total_value == 0:
        return 0

    return asset.current_value / total_value


def update_assets_weight():
    assets = Asset.objects.all()
    for asset in assets:
        asset.initial_weight = get_asset_initial_weight(asset)
        asset.current_weight = get_asset_current_weight(asset)
        
        asset.save()


def update_asset_portfolio(asset, transaction, transaction_deleted=False):
    portfolio = asset.portfolio
    
    if transaction_deleted and transaction.type == Types.BUY:
        portfolio.cash += transaction.value

    elif transaction_deleted and transaction.type == Types.SELL:
        portfolio.cash -= transaction.value

    elif not transaction_deleted and transaction.type == Types.BUY:
        portfolio.cash -= transaction.value

    elif not transaction_deleted and transaction.type == Types.SELL:
        portfolio.cash += transaction.value

    if transaction_deleted:
        portfolio.transactions_cost -= transaction.provision
        portfolio.transactions_counter -= 1
        portfolio.cash += transaction.provision
    else:
        portfolio.transactions_cost += transaction.provision
        portfolio.transactions_counter += 1
        portfolio.cash -= transaction.provision

    p_assets = portfolio.assets.all()
    
    total_current_value = 0
    for p_asset in p_assets:
        total_current_value += p_asset.current_value

    portfolio.value = total_current_value + portfolio.cash
                                          # - snapshot.value
    portfolio.annual_gain = portfolio.value - portfolio.deposit
                                            # / snapshot.value
    portfolio.annual_yield = portfolio.value / portfolio.deposit - 1

    portfolio.save()


def update_asset(asset, transaction, transaction_deleted=False):
    asset.current_price = transaction.price

    if transaction_deleted and transaction.type == Types.BUY:
        asset.total -= transaction.amount
        asset.initial_value -= asset.initial_price * transaction.amount

    elif transaction_deleted and transaction.type == Types.SELL:
        asset.total += transaction.amount
        asset.initial_value += asset.initial_price * transaction.amount

    elif not transaction_deleted and transaction.type == Types.BUY:
        asset.total += transaction.amount
        asset.initial_value += transaction.value

    elif not transaction_deleted and transaction.type == Types.SELL:
        asset.total -= transaction.amount
        asset.initial_value -= asset.initial_price * transaction.amount

    if asset.total > 0:
        asset.initial_price = asset.initial_value / asset.total

    asset.initial_value = asset.initial_price * asset.total

    asset.current_value = asset.current_price * asset.total

    if asset.total == 0:
        asset.gain = 0

    else:
        asset.gain = asset.current_value / asset.initial_value - 1
        
    asset.save()
