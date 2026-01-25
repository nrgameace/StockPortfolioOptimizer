from download_stock_data import download_stocks
from walk_forward_backtest import walk_forward_backtest
import matplotlib.pyplot as plt

def main(tickers, new_stocks = False, initial_value = 10000, num_cycles = 3, num_train_days = 30, num_test_days = 12):

    # Compare predicted values to that of S&P500
    STANDARD_RETURN_RATE = 0.12
    num_days = (num_test_days) * num_cycles
    returns = STANDARD_RETURN_RATE * initial_value * (num_days / 365)
    total_value = returns + initial_value
    print(f"${total_value}")
    x_days_regular = [0,num_test_days * num_cycles]
    y_value_regular = [initial_value, total_value]


    x_days_optimized = [num_test_days * i for i in range(num_cycles+1)]
    y_value_optimized = [initial_value,]

    if new_stocks:
        download_stocks(tickers)
    
    weights, final_values, metrics = walk_forward_backtest(tickers, initial_value, num_cycles, num_train_days, num_test_days)
    print(weights)
    print(final_values)
    print(metrics["CAGR"])
    print(metrics["Sharpe Ratio"])
    print(metrics["Daily Volatility"])

    y_value_optimized = y_value_optimized + final_values

    

    fig, ax = plt.subplots()

    # Optional: set title and labels
    ax.plot(x_days_optimized, y_value_optimized, label="Optimized")
    ax.plot(x_days_regular, y_value_regular, label="S&P500")
    ax.set_title("Portfolio Value v. Time Elapsed")
    ax.set_xlabel("Time Elapsed (Days)")
    ax.set_ylabel("Total Value ($)")
    ax.legend()

    #plt.show()
    fig.savefig("Value30testday5cycle.png", dpi=300, bbox_inches="tight")



if __name__ == "__main__":
    tickers = ["AAPL","MSFT","NVDA","AMZN","JNJ","JPM","XOM","CAT","PG","NEE"]
    new_stocks = False
    main(tickers, new_stocks, initial_value = 10000)
#AAPL,MSFT,NVDA,AMZN,JNJ,JPM,XOM,CAT,PG,NEE