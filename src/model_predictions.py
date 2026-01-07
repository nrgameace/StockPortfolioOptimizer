import pandas as pd
import os
from joblib import load
#from .config import get_data_path, get_models_path
from config import get_data_path, get_models_path


def model_predictions(tickers, day, end_date, horizon = 1):
    models = load_models(tickers)
    data_dir = get_data_path()
    path = os.path.join(data_dir,"TRAINING_DATA.csv")
    df = pd.read_csv(path)
    mu_vector = []

    returns = df[[f"{ticker}_Returns" for ticker in tickers]]

    returns = returns.dropna()
    returns = returns[0:end_date]
    cov_matrix = returns.cov().values  # n x n numpy array


    # Predict next-day return for each ticker
    for i, ticker in enumerate(tickers):
        # Features for prediction: all columns related to the ticker except returns
        features = [col for col in df.columns if ticker in col and "Returns" not in col]
        #df = df.shift(-horizon)
        # Use the last available row as today's features
        last_features = df[features].iloc[[day]]  # double brackets keep it as DataFrame
        pred = models[i].predict(last_features)

        # Store the 1-day ahead prediction
        mu_vector.append(pred[0])

    return mu_vector, cov_matrix





def load_models(tickers):
    model_dir = get_models_path()
    models = []

    for ticker in tickers:
        path = f"{model_dir}/{ticker}_model.pkl"
        model = load(path)
        models.append(model)

    return models


