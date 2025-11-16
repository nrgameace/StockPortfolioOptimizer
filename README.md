# 📈 Stock Portfolio Optimizer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)](https://scikit-learn.org/)
[![CVXPY](https://img.shields.io/badge/CVXPY-Optimization-green.svg)](https://www.cvxpy.org/)

A sophisticated machine learning-driven portfolio optimization system that combines predictive modeling with convex optimization to construct optimal investment portfolios. This project leverages Random Forest regressors for stock price prediction and implements mean-variance optimization with risk constraints to maximize risk-adjusted returns.

## 🎯 Overview

This project implements a complete quantitative finance pipeline that:
- **Predicts** future stock returns using ensemble machine learning models
- **Optimizes** portfolio allocation using modern portfolio theory
- **Balances** expected returns against portfolio risk through convex optimization
- **Supports** multi-asset portfolios with customizable prediction horizons

The system is designed for both research and practical application, demonstrating proficiency in machine learning, optimization theory, and quantitative finance.

## 🏗️ Architecture

```
StockPortfolioOptimizer/
├── src/
│   ├── train_models.py        # Random Forest training pipeline
│   ├── model_predictions.py   # Prediction generation & covariance estimation
│   ├── optimized_weights.py   # Convex optimization solver
│   └── main.py               # End-to-end portfolio construction
├── models/                   # Trained ML models (pkl files)
├── data/
│   └── raw/                 # Historical stock data
├── notebooks/               # Exploratory analysis & visualization
│   ├── portfolio_optimization.ipynb
│   ├── returns_analysis.ipynb
│   └── ticker_data.ipynb
└── results/                # Output visualizations & metrics
```

## 🔬 Methodology

### 1. **Predictive Modeling**
- **Algorithm**: Random Forest Regressor (200 estimators)
- **Features**: Technical indicators derived from historical price data
- **Target**: Future returns over customizable horizon (default: 20 days)
- **Validation**: Time-series aware train-test split to prevent look-ahead bias
- **Metrics**: RMSE and MSE for model evaluation

### 2. **Portfolio Optimization**
The system implements **Markowitz Mean-Variance Optimization** with:
```python
maximize: μᵀw - λ·wᵀΣw
subject to: Σwᵢ = 1, wᵢ ≥ 0
```
Where:
- `μ` = Expected returns vector (from ML predictions)
- `Σ` = Covariance matrix (estimated from historical returns)
- `w` = Portfolio weights
- `λ` = Risk aversion parameter (default: 100)

**Constraints**:
- Full investment: weights sum to 1
- Long-only: no short-selling (w ≥ 0)

### 3. **Risk Analysis**
- **Expected Return**: Computed as weighted average of predicted returns
- **Portfolio Volatility**: Derived from asset covariance matrix
- **Sharpe Ratio**: Risk-adjusted return metric for performance evaluation

## 🚀 Key Features

- **Scalable ML Pipeline**: Modular design allows easy integration of new stocks
- **Convex Optimization**: CVXPY framework ensures globally optimal solutions
- **Risk Management**: Configurable risk aversion with variance penalization
- **Backtesting Support**: Time-series split prevents data leakage
- **Reproducible Results**: Seeded random states for consistent model training

## 📊 Supported Assets

Current implementation includes 10 diverse stocks across sectors:
- **Technology**: AAPL, MSFT, NVDA, AMZN
- **Healthcare**: JNJ
- **Financial**: JPM
- **Energy**: XOM, NEE
- **Industrial**: CAT
- **Consumer Goods**: PG

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip or conda package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/StockPortfolioOptimizer.git
cd StockPortfolioOptimizer
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install numpy pandas scikit-learn cvxpy joblib jupyter matplotlib seaborn
```

### Dependencies
```
numpy           # Numerical computing
pandas          # Data manipulation
scikit-learn    # Machine learning models
cvxpy           # Convex optimization
joblib          # Model serialization
jupyter         # Notebooks for analysis
matplotlib      # Visualization
seaborn         # Statistical plots
```

## 💻 Usage

### Training Models

Train Random Forest models for all tickers:
```bash
cd src
python train_models.py
```

This will:
1. Load historical stock data from `data/raw/TRAINING_DATA.csv`
2. Train separate models for each ticker
3. Save trained models to `models/` directory
4. Print validation metrics (MSE, RMSE)

### Generating Optimal Portfolio

Run the complete optimization pipeline:
```bash
python main.py
```

**Output Example:**
```
Optimal weights: [0.15 0.22 0.18 0.12 0.08 0.11 0.05 0.06 0.02 0.01]

Expected portfolio return: 3.45%
Portfolio volatility: 1.82%
Sharpe ratio: 1.895
```

### Custom Configuration

Modify parameters in `main.py`:
```python
tickers = ["AAPL", "MSFT", "NVDA", ...]  # Asset universe
horizon = 20                              # Prediction window (days)
risk_aversion = 100                       # Risk tolerance (higher = more conservative)
```

## 📈 Performance Metrics

The optimizer provides comprehensive portfolio analytics:

| Metric | Description |
|--------|-------------|
| **Optimal Weights** | Allocation percentages for each asset |
| **Expected Return** | Predicted portfolio return over horizon |
| **Volatility** | Portfolio standard deviation (risk measure) |
| **Sharpe Ratio** | Return per unit of risk |

## 🔍 Technical Highlights

### Machine Learning
- **Ensemble Learning**: Leverages Random Forest's robustness to overfitting
- **Feature Engineering**: Extracts technical indicators from raw price data
- **Cross-Validation**: Time-aware splitting maintains temporal relationships

### Optimization
- **Convex Programming**: Guarantees global optimality through quadratic programming
- **Risk-Return Tradeoff**: Explicit risk aversion parameter for customization
- **Constraint Handling**: Enforces practical investment constraints

### Software Engineering
- **Modular Design**: Clean separation of concerns across modules
- **Reproducibility**: Seeded randomness and versioned models
- **Scalability**: Easy to extend to new assets or features

## 📚 Notebooks

Explore the analysis notebooks for deeper insights:

- **`portfolio_optimization.ipynb`**: End-to-end optimization workflow
- **`returns_analysis.ipynb`**: Statistical analysis of asset returns
- **`ticker_data.ipynb`**: Data exploration and preprocessing

## 🧪 Future Enhancements

- [ ] Implement transaction cost modeling
- [ ] Add support for dynamic rebalancing strategies
- [ ] Integrate real-time data feeds via APIs (Alpha Vantage, Yahoo Finance)
- [ ] Develop backtesting framework with rolling window validation
- [ ] Incorporate alternative models (LSTM, Transformer architectures)
- [ ] Add factor models (Fama-French) for return attribution
- [ ] Implement Black-Litterman model for Bayesian optimization
- [ ] Create interactive dashboard with Streamlit/Dash

## 📖 Theoretical Background

### Mean-Variance Optimization
Based on Harry Markowitz's Modern Portfolio Theory (1952), which established the foundation for quantitative portfolio management. The framework balances expected returns against portfolio variance under the assumption of normally distributed returns.

### Random Forest Regression
An ensemble learning method that constructs multiple decision trees and aggregates their predictions, reducing overfitting while capturing non-linear relationships in financial time series.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Alternative optimization solvers (e.g., robust optimization)
- Additional asset classes (bonds, commodities, crypto)
- Enhanced feature engineering techniques
- Performance benchmarking against market indices

## 📄 License

This project is available for educational and research purposes.

## 👤 Author

**Nickolas Regas**

This project demonstrates expertise in:
- Quantitative Finance & Portfolio Theory
- Machine Learning & Statistical Modeling
- Optimization & Operations Research
- Python Software Engineering
- Data Science & Analytics

---

⭐ If you find this project interesting, please consider starring the repository!
