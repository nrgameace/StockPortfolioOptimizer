import pandas as pd
import os
from joblib import load


def model_predictions(tickers, prediction_horizon = 15 ):
    predicted_returns = {ticker: [] for ticker in tickers}

def load_models(tickers):
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    model_dir = os.path.join(project_root, "StockPortfolioOptimizer","models")
    models = []

    for ticker in tickers:
        path = f"{model_dir}/{ticker}_model.pkl"
        model = load(path)
        models.append(model)
    print(len(models))

tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "JNJ", "JPM", "XOM", "CAT", "PG", "NEE"]
load_models(tickers)
