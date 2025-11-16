from model_predictions import model_predictions
from optimized_weights import optimizer
import numpy as np

def main(tickers, horizon = 20):
    mu_array, cov_matrix = model_predictions(tickers)

    print(optimizer(mu_array, cov_matrix))

    eps = 1e-8
    w = np.maximum(mu_array, eps)        # set tiny/negative -> eps
    w = w / w.sum()                   # renormalize to sum to 1

    # 2) Metrics
    exp_return = float(mu_array @ w)        # expected portfolio return (fraction)
    vol = float(np.sqrt(w @ cov_matrix @ w))  # portfolio std dev (fraction)
    sharpe = exp_return / vol if vol > 0 else np.nan

    # 3) Print nicely
    for t, weight in enumerate(w):
        print(f"{t:2d}: {weight*100:6.2f}%")
    print(f"\nSum weights: {w.sum():.6f}")
    print(f"Expected return (horizon): {exp_return:.6%}")
    print(f"Volatility (horizon): {vol:.6%}")
    print(f"Sharpe (horizon): {sharpe:.3f}")




if __name__ == "__main__":
    tickers = ["AAPL","MSFT","NVDA","AMZN","JNJ","JPM","XOM","CAT","PG","NEE"]
    main(tickers, 20)
