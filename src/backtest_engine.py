# Backtest Engine

class BacktestEngine:

    def __init__(self, weights, initial_value, filepath):
        self.weights = weights
        self.initial_value = initial_value
        self.filepath = filepath
        

    def simulate_one_day(self):
        pass

    def run_backtest(self, num_days):
        ending_price = self.initial_value
        for i in range(num_days):
            new_price = self.simulate_one_day()

    def compute_metrics():
        pass
