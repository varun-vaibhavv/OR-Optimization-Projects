import numpy as np
from scipy.optimize import curve_fit

def exponential_model(x, a, b):
    return a * np.exp(b * x)

def nonlinear_curve_fit(x, y):
    params, cov = curve_fit(exponential_model, x, y, maxfev=5000)
    y_fit = exponential_model(x, *params)
    return params, cov, y_fit
