import numpy as np
import matplotlib.pyplot as plt

def plot_feasible_region():
    x1 = np.linspace(0, 6, 400)

    x2_c1 = (8 - x1) / 2
    x2_c2 = (12 - 3*x1) / 2
    x2_zero = np.zeros_like(x1)

    plt.figure(figsize=(8,6))
    plt.plot(x1, x2_c1, label=r'$x_1 + 2x_2 = 8$')
    plt.plot(x1, x2_c2, label=r'$3x_1 + 2x_2 = 12$')
    plt.plot(x1, x2_zero, label=r'$x_2 = 0$')

    x2_feasible = np.maximum(0, np.minimum(x2_c1, x2_c2))
    plt.fill_between(x1, x2_feasible, alpha=0.3)

    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.title("Feasible Region of the Linear Programming Problem")
    plt.legend()
    plt.grid(True)
    plt.show()
