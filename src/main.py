from model_predictions import model_predictions
from optimized_weights import optimizer
import numpy as np
from backtest_engine import BacktestEngine
import os

def main(tickers, horizon = 20):



    mu_array, cov_matrix = model_predictions(tickers)

    print(optimizer(mu_array, cov_matrix))

    eps = 1e-8
    w = np.maximum(mu_array, eps)        
    w = w / w.sum()                   # renormalize to sum to 1

    # Metrics
    exp_return = float(mu_array @ w)        # expected portfolio return 
    vol = float(np.sqrt(w @ cov_matrix @ w))  # portfolio std dev
    sharpe = exp_return / vol if vol > 0 else np.nan

    # Print Metrics
    for t, weight in enumerate(w):
        print(f"{t:2d}: {weight*100:6.2f}%")
    print(f"\nSum weights: {w.sum():.6f}")
    print(f"Expected return (horizon): {exp_return:.6%}")
    print(f"Volatility (horizon): {vol:.6%}")
    print(f"Sharpe (horizon): {sharpe:.3f}")

    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    data_dir = os.path.join(project_root, "StockPortfolioOptimizer", "data", "raw")
    path = os.path.join(data_dir,"TRAINING_DATA.csv")

    optimized_backtester = BacktestEngine(w,10000, path, tickers)
    print(optimized_backtester.run_backtest(100))

    even_weights = np.ones(len(tickers)) / len(tickers)
    even_backtester = BacktestEngine(even_weights,10000, path, tickers)
    print(even_backtester.run_backtest(100))




if __name__ == "__main__":
    tickers = ["AAPL","MSFT","NVDA","AMZN","JNJ","JPM","XOM","CAT","PG","NEE"]
    main(tickers, 20)
