# Backtest Engine
import pandas as pd
import numpy as np
import os

class BacktestEngine:

    # Constructor for Backtest Engine
    def __init__(self, weights, initial_value, tickers):
        # Define dataset path
        project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
        data_dir = os.path.join(project_root, "StockPortfolioOptimizer", "data", "raw")
        path = os.path.join(data_dir,"TRAINING_DATA.csv")

        # Initialize instance variables
        self.weights = np.array(weights)
        self.data = pd.read_csv(path)
        self.day = 0
        self.current_value = initial_value
        self.values = [initial_value]
        self.tickers = tickers
      
    # Simulates the return for one day and calculates the new portfolio value 
    def simulate_one_day(self):
        day_data = self.data.iloc[self.day]
        returns_for_day = []

        for ticker in self.tickers:
            returns_for_day.append(day_data[f"{ticker}_Returns"])
        
        weighted_return = np.dot(self.weights, returns_for_day)
        self.current_value = self.current_value * (1 + weighted_return)
        self.values.append(self.current_value)


    # Simulates the given weights over a specified amount of time
    def run_backtest(self, num_days):
        for i in range(num_days):
            if (i < len(self.data)):
                self.simulate_one_day()
                self.day += 1

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
        "CAGR": cagr,
        "Daily Volatility": daily_volatility,
        "Sharpe Ratio": sharpe_ratio
        }
