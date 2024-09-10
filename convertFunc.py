def toWAL(expr):
    expr = expr.replace('+', '||')
    expr = expr.replace('*', '&&')
    return expr

def toPY(expr):
    expr = expr.replace('||', '+')
    expr = expr.replace('&&', '*')
    return expr