from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import os
import joblib

def train_models(tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "JNJ", "JPM", "XOM", "CAT", "PG", "NEE"]):
    #Define the path to the data
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    data_dir = os.path.join(project_root, "data", "raw")
    model_dir = os.path.join(project_root, "models")
    os.makedirs(data_dir, exist_ok=True)

    path = os.path.join(data_dir,"TRAINING_DATA.csv")
    train_data = pd.read_csv(path)

    for ticker in tickers:
        features = [col for col in train_data.columns if "AAPL" in col and "Close" not in col]
        x = train_data[features]
        y = train_data[f'{ticker}_Close'].shift(-1)
        x, y = x[:-1], y[:-1]

        X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = .2, shuffle = False)
        model = RandomForestRegressor(n_estimators = 200, random_state = 42)
        model.fit(X_train, y_train)


        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        print(f"{ticker} Test MSE: {mse:.4f}")

        joblib.dump(model, f"{model_dir}/{ticker}_model.pkl")
        print(f"{ticker} model trained and saved.")


if __name__ == "__main__":
    tickers = ["AAPL","MSFT","NVDA","AMZN","JNJ","JPM","XOM","CAT","PG","NEE"]
    train_models(tickers)
