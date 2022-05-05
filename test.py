exchanges = ["BINANCE", "KUCOIN", "BITTREX", "COINEX"]
currencies = ['BTC', 'USDT']

def symbol_to_tradingview(symbol):
    one_symbol_watchlist = []
    for exchange in exchanges:
        for currency in currencies:
            current_pair = ""
            one_symbol_watchlist.append(f"{exchange}:{symbol}{currency}")
    return one_symbol_watchlist


print(len(symbol_to_tradingview('ADA')))

