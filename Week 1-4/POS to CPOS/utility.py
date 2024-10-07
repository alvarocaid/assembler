def count_components(expr, delimiter):
    if delimiter not in ['*', '+']:
        raise ValueError("Delimiter must be '*' or '+'")
    return len(expr.split(delimiter))

