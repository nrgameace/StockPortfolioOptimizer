# Backtest Engine
import pandas as pd
import numpy as np
import os
#from .config import get_data_path
from config import get_data_path
class BacktestEngine:

    # Constructor for Backtest Engine
    def __init__(self, initial_value: float, tickers: list, start_date):
        # Define dataset path
        data_dir = get_data_path()
        path = os.path.join(data_dir,"TRAINING_DATA.csv")

        # Initialize instance variables
        self.data = pd.read_csv(path)
        self.day = start_date
        self.current_value = initial_value
        self.values = [initial_value]
        self.tickers = tickers
      
    # Simulates the return for one day and calculates the new portfolio value 
    def simulate_one_day(self, weights):
        day_data = self.data.iloc[self.day]
        returns_for_day = []

        for ticker in self.tickers:
            returns_for_day.append(day_data[f"{ticker}_Returns"])
        
        weighted_return = np.dot(weights[0], returns_for_day)
        self.current_value = self.current_value * (1 + weighted_return)
        self.values.append(self.current_value)
        self.day += 1

    def final_portfolio_value(self):
        return self.current_value

    # Computes several metrics based on backtesting results
    def compute_metrics(self):
        total_return = self.current_value / self.values[0] - 1

        daily_returns = np.diff(self.values) / self.values[:-1]

        num_days = len(self.values) - 1
        cagr = (self.current_value / self.values[0])**(252 / num_days) - 1

        daily_volatility = np.std(daily_returns)

        sharpe_ratio = (np.mean(daily_returns) / daily_volatility) * np.sqrt(252)

        return {
        "Total Return": total_return,
        "Ending Value": self.current_value,
        "CAGR": cagr,
        "Daily Volatility": daily_volatility,
        "Sharpe Ratio": sharpe_ratio
        }
