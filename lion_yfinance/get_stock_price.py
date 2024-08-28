from yfinance import Ticker


def get_stock_prices(symbol, **kwargs):

    stock = Ticker(symbol)
    hist = stock.history(**kwargs)
    return hist
