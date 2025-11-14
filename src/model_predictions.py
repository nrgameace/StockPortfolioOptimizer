import pandas as pd
import os
from joblib import load
import numpy as np
from sklearn.ensemble import RandomForestRegressor


def model_predictions(tickers):
    models = load_models(tickers)
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    model_dir = os.path.join(project_root, "StockPortfolioOptimizer","data","raw")
    path = os.path.join(model_dir,"TRAINING_DATA.csv")
    dataset = pd.read_csv(path)
    mu_vector = []

    for i in range(0,10):
        model = models[i]
        features = [col for col in dataset.columns if tickers[i] in col and "Close" not in col]
        last_features = dataset[features].iloc[-1:]
        predicted_price = model.predict(last_features)[0]

        last_price = dataset[f"{tickers[i]}_Close"].iloc[-1]
        predicted_return = (predicted_price - last_price) / last_price
        mu_vector.append(predicted_return)


    return mu_vector





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
mu_vector = model_predictions(tickers)
print(mu_vector)
