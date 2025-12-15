from backtest_engine import BacktestEngine
from train_models import train_models
from model_predictions import model_predictions
from optimized_weights import optimizer


def walk_forward_backtest(tickers ,initial_value, num_cycles, num_train_days, num_test_days):


    end_train_row = num_train_days
    weights = []
    ending_portfolio_values = []

    for i in range(num_cycles):  
        backtestEngine = BacktestEngine(initial_value, tickers, end_train_row + 1)
        train_models(tickers, end_row = end_train_row)
        for j in range(num_test_days):
            mu_vector, cov_matrix = model_predictions(tickers, end_train_row + j, end_train_row)
            weights = optimizer(mu_vector, cov_matrix)

            backtestEngine.simulate_one_day(weights)



        end_train_row = end_train_row + num_train_days + num_test_days 

        print(backtestEngine.compute_metrics())
        ending_portfolio_values.append(backtestEngine.final_portfolio_value())

    
    return weights, ending_portfolio_values

