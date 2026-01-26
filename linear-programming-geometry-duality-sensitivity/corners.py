def objective(x1, x2):
    return 3*x1 + 5*x2

def evaluate_corners():
    points = {
        "O": (0, 0),
        "A": (0, 4),
        "B": (2, 3),
        "C": (4, 0)
    }

    results = {}
    for name, (x1, x2) in points.items():
        results[name] = {
            "x1": x1,
            "x2": x2,
            "Z": objective(x1, x2)
        }
    return results
