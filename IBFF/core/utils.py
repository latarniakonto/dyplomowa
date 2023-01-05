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
    from queue import Queue
    temp_asset = TempAsset()

    transactions = Transaction.objects.filter(
        portfolio=asset.portfolio, ticker=asset.ticker, date__lte=date
    ).order_by('date', 'created_at')
    if len(transactions) == 0:
        return temp_asset

    assert transactions[0].type == Types.BUY

    sell_queue = Queue()
    temp_asset.ticker = asset.ticker
    for transaction in transactions:
        if transaction.type == Types.BUY:
            temp_asset.total += transaction.amount
            temp_asset.initial_value += transaction.amount * transaction.price
            sell_queue.put([transaction.amount, transaction.price])

        else:
            temp_asset.total -= transaction.amount
            initial_value = 0
            while transaction.amount > 0:
                diff = transaction.amount - sell_queue.queue[0][0]
                if diff >= 0:
                    initial_value += sell_queue.queue[0][0] * sell_queue.queue[0][1]
                    transaction.amount -= sell_queue.queue[0][0]
                    sell = sell_queue.get()
                
                else:
                    initial_value += transaction.amount * sell_queue.queue[0][1]
                    sell_queue.queue[0][0] -= transaction.amount
                    transaction.amount = 0

            temp_asset.initial_value -= initial_value
    
    return temp_asset
