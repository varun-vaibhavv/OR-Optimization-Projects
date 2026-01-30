from pulp import LpMaximize, LpProblem, LpVariable, value, PULP_CBC_CMD

def cost_sensitivity():
    model = LpProblem("Cost_Sensitivity", LpMaximize)

    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)

    model += 4*x1 + 5*x2
    model += x1 + 2*x2 <= 8
    model += 3*x1 + 2*x2 <= 12

    model.solve(PULP_CBC_CMD(msg=False))

    return value(x1), value(x2), value(model.objective)
