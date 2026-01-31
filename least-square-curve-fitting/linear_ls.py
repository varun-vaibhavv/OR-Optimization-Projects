import numpy as np

def linear_least_squares(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    coeffs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    a_hat, b_hat = coeffs
    y_fit = a_hat * x + b_hat
    return a_hat, b_hat, y_fit
