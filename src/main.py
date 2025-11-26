from download_stock_data import download_stocks
from walk_forward_backtest import walk_forward_backtest

def main(tickers, horizon = 20, new_stocks = False):

    if new_stocks:
        download_stocks(tickers)

    weights, final_values = walk_forward_backtest(tickers, 10000, 3, 120, 30)
    print(weights)
    print(final_values)

if __name__ == "__main__":
    tickers = ["AAPL","MSFT","NVDA","AMZN","JNJ","JPM","XOM","CAT","PG","NEE"]
    new_stocks = False
    main(tickers, 20, new_stocks)
