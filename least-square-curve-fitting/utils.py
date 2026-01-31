import matplotlib.pyplot as plt

def plot_data(x, y, y_ref=None, title=""):
    plt.scatter(x, y, label="Observed data")
    if y_ref is not None:
        plt.plot(x, y_ref, label="Reference", color="black")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.legend()
    plt.show()

def plot_fit(x, y, y_fit, title=""):
    plt.scatter(x, y, label="Observed data")
    plt.plot(x, y_fit, label="Fitted curve", color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.legend()
    plt.show()

def plot_residuals(x, residuals, title=""):
    plt.scatter(x, residuals)
    plt.axhline(0, color="black", linestyle="--")
    plt.xlabel("x")
    plt.ylabel("Residual")
    plt.title(title)
    plt.show()
