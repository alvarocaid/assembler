def toWAL(expr):
    expr = expr.replace('+', '||').replace('*', '&&')
    return expr

def toPY(expr):
    expr = expr.replace('||', '+').replace('&&', '*')
    return expr

def PYtoLatexCode(expr):
    expr = expr.replace('+', '\lor').replace('*', '\land').replace('!', '\lnot')
    return expr