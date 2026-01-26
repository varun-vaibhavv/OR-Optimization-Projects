from pulp import LpMaximize, LpProblem, LpVariable, value

def solve_dual():
    dual = LpProblem("Dual_LP", LpMaximize)

    y1 = LpVariable("y1", lowBound=0)
    y2 = LpVariable("y2", lowBound=0)

    dual += -(8*y1 + 12*y2)
    dual += y1 + 3*y2 >= 3
    dual += 2*y1 + 2*y2 >= 5

    dual.solve()

    return {
        "y1": value(y1),
        "y2": value(y2),
        "dual_value": -value(dual.objective)
    }
