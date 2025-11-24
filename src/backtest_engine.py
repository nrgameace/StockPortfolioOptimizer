# Backtest Engine
import pandas as pd
import numpy as np

class BacktestEngine:

    def __init__(self, weights, initial_value, filepath, tickers):
        self.weights = np.array(weights)
        self.data = pd.read_csv(filepath)
        self.day = 0
        self.current_value = initial_value
        self.values = [initial_value]
        self.tickers = tickers

        

    def simulate_one_day(self):
        day_data = self.data.iloc[self.day]
        returns_for_day = []

        for ticker in self.tickers:
            returns_for_day.append(day_data[f"{ticker}_Close"])
        
        weighted_return = np.dot(self.weights, returns_for_day)
        self.current_value = self.current_value * (1 + weighted_return)
        self.values.append(self.current_value)
        return self.current_value

            


    def run_backtest(self, num_days):
        
        for i in range(num_days):
            if (i < len(self.data)):
                self.simulate_one_day()
                self.day += 1

        return self.current_value

    def compute_metrics():
        pass
