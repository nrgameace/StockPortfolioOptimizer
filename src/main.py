from model_predictions import model_predictions
from optimized_weights import optimizer
import numpy as np
from backtest_engine import BacktestEngine
from train_models import train_models
from download_stock_data import download_stocks
from walk_forward_backtest import walk_forward_backtest

def main(tickers, horizon = 20, new_stocks = False):

    if new_stocks:
        download_stocks(tickers)
        train_models(tickers, horizon)
    '''
    mu_array, cov_matrix = model_predictions(tickers)

    print(optimizer(mu_array, cov_matrix))

    w = optimizer(mu_array, cov_matrix)  # get optimized weights               

    # Metrics
    # expected portfolio return 
    exp_return = float(mu_array @ w)        
    # portfolio std dev
    vol = float(np.sqrt(w @ cov_matrix @ w))  
    sharpe = exp_return / vol if vol > 0 else np.nan

    # Print Metrics
    for t, weight in enumerate(w):
        print(f"{t:2d}: {weight*100:6.2f}%")
    print(f"\nSum weights: {w.sum():.6f}")
    print(f"Expected return (horizon): {exp_return:.6%}")
    print(f"Volatility (horizon): {vol:.6%}")
    print(f"Sharpe (horizon): {sharpe:.3f}")

    # Backtesting
    optimized_backtester = BacktestEngine(w,10000, tickers)
    print(optimized_backtester.run_backtest(60))

    even_weights = np.ones(len(tickers)) / len(tickers)
    even_backtester = BacktestEngine(even_weights,10000, tickers)
    print(even_backtester.run_backtest(60))

    '''

    weights, final_value = walk_forward_backtest(tickers, 10000, 3, 120, 30)
    print(weights)
    print(final_value)

if __name__ == "__main__":
    tickers = ["AAPL","MSFT","NVDA","AMZN","JNJ","JPM","XOM","CAT","PG","NEE"]
    new_stocks = False
    main(tickers, 20, new_stocks)
