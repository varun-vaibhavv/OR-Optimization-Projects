from pulp import LpMaximize, LpProblem, LpVariable, value, PULP_CBC_CMD

def solve_primal():
    model = LpProblem("Primal_LP", LpMaximize)

    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)

    model += 3*x1 + 5*x2
    model += x1 + 2*x2 <= 8
    model += 3*x1 + 2*x2 <= 12

    model.solve(PULP_CBC_CMD(msg=False))

    return {
        "x1": value(x1),
        "x2": value(x2),
        "Z": value(model.objective),
        "shadow_prices": {n: c.pi for n, c in model.constraints.items()},
        "reduced_costs": {v.name: v.dj for v in model.variables()}
    }
