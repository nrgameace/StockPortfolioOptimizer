from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import os
import joblib
import numpy as np

def train_models(tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "JNJ", "JPM", "XOM", "CAT", "PG", "NEE"], horizon = 20):

    #Define the path to the data
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    data_dir = os.path.join(project_root, "StockPortfolioOptimizer", "data", "raw")
    model_dir = os.path.join(project_root, "StockPortfolioOptimizer","models")
    os.makedirs(data_dir, exist_ok=True)

    path = os.path.join(data_dir,"TRAINING_DATA.csv")
    train_data = pd.read_csv(path)
    

    for ticker in tickers:
        df = train_data.copy()
        df = df[df[f"{ticker}_Close"] != 0]  # remove rows with missing/0 returns

        # Features 
        features = [col for col in df.columns if ticker in col and "Close" not in col]
        x = df[features]

        # Target is the future return over horizon days
        y = df[f"{ticker}_Close"].shift(-horizon)

        # Remove last `horizon` rows because target is NaN after shift
        x, y = x[:-horizon], y[:-horizon]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

        # Train Random Forest
        model = RandomForestRegressor(n_estimators=200, random_state=42)
        model.fit(X_train, y_train)

        # Predictions and metrics
        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        rmse = np.sqrt(mse)
        print(f"{ticker} Test MSE: {mse:.6f}, RMSE: {rmse:.6f}")

        # Save model
        joblib.dump(model, os.path.join(model_dir, f"{ticker}_model.pkl"))
        print(f"{ticker} model trained and saved.\n")


if __name__ == "__main__":
    tickers = ["AAPL","MSFT","NVDA","AMZN","JNJ","JPM","XOM","CAT","PG","NEE"]
    train_models(tickers, 20)
