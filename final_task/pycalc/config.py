import operator
import math

FLAG_LOG = None
FLAG_ROUND = None
CONSTANTS = {"pi": math.pi,
             "e": math.e,
             "tau": math.tau,
             "inf": math.inf,
             "nan": math.nan, }
MATH_OPERATORS = {">": (1, operator.gt), "<": (1, operator.lt),
                  ">=": (1, operator.ge), "<=": (1, operator.le),
                  "!=": (1, operator.ne), "==": (1, operator.eq),
                  "+": (2, operator.add), "-": (2, operator.sub),
                  "neg": (2, operator.neg), "*": (3, operator.mul),
                  "/": (3, operator.truediv), "//": (3, operator.floordiv),
                  "%": (3, operator.mod), "^": (4, operator.pow), }

FUNCTIONS = {"abs": (5, abs), "round": (5, round), }

for key, value in math.__dict__.items():
    if '__' in key or key in CONSTANTS:
        continue
    FUNCTIONS[key] = (5, value)

FUNCTIONS_AND_OPERATORS = {**MATH_OPERATORS, **FUNCTIONS}
