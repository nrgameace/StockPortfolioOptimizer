import pandas as pd
import os
import joblib

def model_predictions(tickers, prediction_horizon = 15 ):
    predicted_returns = {ticker: [] for ticker in tickers}

