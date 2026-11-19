import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    l = []
    for xl in x:
        if xl>0:
            l.append(xl)
        else:
            l.append(alpha * (math.exp(xl) -1))
    return l