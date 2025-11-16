import pandas as pd
import os
from joblib import load


def model_predictions(tickers, horizon = 20):
    models = load_models(tickers)
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    model_dir = os.path.join(project_root, "StockPortfolioOptimizer","data","raw")
    path = os.path.join(model_dir,"TRAINING_DATA.csv")
    df = pd.read_csv(path)
    mu_vector = []

    returns = df[[f"{ticker}_Close" for ticker in tickers]]

    returns = returns.dropna()
    cov_matrix = returns.cov().values  # n x n numpy array

    print("Covariance matrix:")
    print(cov_matrix)

    for i, ticker in enumerate(tickers):
        # Prepare features for prediction
        features = [col for col in df.columns if ticker in col and "Close" not in col]
        last_features = df[features].iloc[-horizon:]  # last `horizon` rows
        pred = models[i].predict(last_features)

        # Take the last prediction as 20-day ahead return
        mu_vector.append(pred[-1])

    return mu_vector, cov_matrix





def load_models(tickers):
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    model_dir = os.path.join(project_root, "StockPortfolioOptimizer","models")
    models = []

    for ticker in tickers:
        path = f"{model_dir}/{ticker}_model.pkl"
        model = load(path)
        models.append(model)

    return models




tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "JNJ", "JPM", "XOM", "CAT", "PG", "NEE"]
mu_vector, matrix = model_predictions(tickers)
print(mu_vector)
print(matrix)
