def future_date(date):
    import datetime
    today = datetime.date.today()
    
    if today.year > date.year:
        return True
    
    elif today.year < date.year:
        return False
    
    else:
        if today.month > date.month:
            return True

        elif today.month < date.month:
            return False
        
        else:
            return today.day < date.day


def get_asset_to_date(asset, date):
    from transactions.models import Transaction, Types
    from assets.models import TempAsset
    temp_asset = TempAsset()
    temp_asset.ticker = asset.ticker

    transactions = Transaction.objects.filter(
        ticker=temp_asset.ticker, date__lte=date        
    )
    for transaction in transactions:
        if transaction.type == Types.BUY:
            temp_asset.total += transaction.amount
            temp_asset.initial_value += transaction.amount * transaction.price
        
        else:
            temp_asset.total -= transaction.amount
            temp_asset.initial_value -= transaction.amount * transaction.price

    return temp_asset
