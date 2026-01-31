import numpy as np

def generate_data(n=30, seed=42):
    np.random.seed(seed)
    x = np.linspace(0, 10, n)
    y_true = 2.5 * x + 1.0
    noise = np.random.normal(0, 2.0, size=len(x))
    y = y_true + noise
    return x, y, y_true
