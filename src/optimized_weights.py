import cvxpy as cp


def optimizer(mu_vector: list, covariance_matrix):

    n = len(mu_vector)
    w = cp.Variable(n)  # weights

    # Mean-variance optimization
    risk_aversion = 100  # Set higher to target weights with less risk
    objective = cp.Maximize(mu_vector @ w - risk_aversion * cp.quad_form(w, covariance_matrix))

    # Constraints: weights sum to 1, no short-selling, no stock can dominate over 40%
    constraints = [cp.sum(w) == 1, w >= 0.05, w <= .40]

    prob = cp.Problem(objective, constraints)
    prob.solve()

    expected_portfolio_return = mu_vector @ w.value
    portfolio_variance = w.value.T @ covariance_matrix @ w.value

    print("Optimal weights:", w.value)
    print("Expected portfolio return:", expected_portfolio_return)
    print("Portfolio variance:", portfolio_variance)
    return w.value, expected_portfolio_return, portfolio_variance