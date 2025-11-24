from backtest_engine import BacktestEngine

def walk_forward_backtest(self, tickers ,initial_value, num_cycles, num_train_days, num_test_days):


    end_train_row = num_train_days
    results = []
    weights = []
    for i in range(num_cycles):


        
        backtestEngine = BacktestEngine(weights, tickers)
    # Initial values 
    # Define a period for train and test - 4 month train, 2 month test
    # Repeat for 4 years
    # Retrain model each time and calculate returns v even weight returns
    # Save final models

        end_train_row = end_train_row + num_train_days + num_test_days 

    
    return results

