import yfinance as yf
import pandas as pd
import time
from .config import get_data_path
import os
from datetime import date

def download_next_day_data(tickers: list):
    all_data = pd.DataFrame()
    df_list = []
    for ticker in tickers:
        data = yf.download(ticker, period="2mo",auto_adjust=True)
        # data = yf.download(ticker, start=currentDate - timedelta(days=1), end=currentDate, auto_adjust=True)
        # Keep only Return and Volume
        print(data)
        data['Returns'] = data['Close']
        features = data[['Returns', 'Volume']].copy()
        features.columns = [f"{ticker}_Returns", f"{ticker}_Volume"]
        df_list.append(features)
        
        time.sleep(5)  # Avoid hitting API limits

    all_data = pd.concat(df_list, axis=1)
    

    if all_data.empty:
        raise ValueError("All data empty. Please check tickers or api rate limit")
    else:
        data_dir = get_data_path()
        current_day = date.today()
        path = os.path.join(data_dir,f"{current_day}.csv")
        all_data.to_csv(path, index=False)

    return all_data