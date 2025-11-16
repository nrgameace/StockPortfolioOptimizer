import numpy as np
import cvxpy as cp


def optimizer(mu_vector, covariance_matrix):

    n = len(mu_vector)
    w = cp.Variable(n)  # weights

    # Mean-variance optimization
    risk_aversion = 100  # higher = more risk-averse
    objective = cp.Maximize(mu_vector @ w - risk_aversion * cp.quad_form(w, covariance_matrix))

    # Constraints: weights sum to 1, no short-selling
    constraints = [cp.sum(w) == 1, w >= 0]

    prob = cp.Problem(objective, constraints)
    prob.solve()

    print("Optimal weights:", w.value)
    print("Expected portfolio return:", mu_vector @ w.value)
    print("Portfolio variance:", w.value.T @ covariance_matrix @ w.value)
    return w.value