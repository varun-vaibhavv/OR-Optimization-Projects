from pulp import LpMaximize, LpProblem, LpVariable, value

def rhs_sensitivity():
    model = LpProblem("RHS_Sensitivity", LpMaximize)

    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)

    model += 3*x1 + 5*x2
    model += x1 + 2*x2 <= 9
    model += 3*x1 + 2*x2 <= 12

    model.solve()

    return value(x1), value(x2), value(model.objective)
