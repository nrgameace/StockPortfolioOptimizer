from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import os
import joblib

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
        df = df[df[f"{ticker}_Close"] != 0] 
        features = [col for col in df.columns if ticker in col and "Close" not in col]
        x = df[features]
        future_price = df[f'{ticker}_Close'].shift(-horizon)
        y = (future_price - df[f"{ticker}_Close"]) / df[f"{ticker}_Close"]
        x, y = x[:-horizon], y[:-horizon]

        X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = .2, shuffle = False)
        model = RandomForestRegressor(n_estimators = 200, random_state = 42)
        model.fit(X_train, y_train)


        # Predictions
        preds = model.predict(X_test)
        
        # Compute MSE and RMSE in price units
        mse = mean_squared_error(y_test, preds)
        rmse = mse ** 0.5

        print(f"{ticker} Test MSE: {mse:.6f}, RMSE: {rmse:.6f}")

        # Save model
        joblib.dump(model, os.path.join(model_dir, f"{ticker}_model.pkl"))
        print(f"{ticker} model trained and saved.\n")


if __name__ == "__main__":
    tickers = ["AAPL","MSFT","NVDA","AMZN","JNJ","JPM","XOM","CAT","PG","NEE"]
    train_models(tickers, 20)
