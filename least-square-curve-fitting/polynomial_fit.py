import numpy as np

def polynomial_fit(x, y, degree=2):
    coeffs = np.polyfit(x, y, deg=degree)
    y_poly = np.polyval(coeffs, x)
    return coeffs, y_poly
