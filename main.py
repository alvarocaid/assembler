import re
from convertFunc import toPY, toWAL

def extract_components(expr, variables):
    """
    Extracts components from the POS expression as a list of lists.
    Each component is a list containing variables and their negations.
    """
    expr = expr.replace(' ', '').replace('+', ' + ').replace('*', ' * ').replace('(', '').replace(')', '')
    clauses = [clause.strip() for clause in expr.split('*')]
    
    components = []
    for clause in clauses:
        clause_vars = re.split(r'\s*\+\s*', clause)
        components.append(clause_vars)
    
    # Sort each component based on the order of variables
    components = [sorted(component, key=lambda x: variables.index(x.strip('!'))) for component in components]
    return components

def expand_component(component, variables):
    """
    Recursively expands a component to include all variables in the correct order.
    """
    expanded_components = [component]  # Start with the original component

    for var in variables:
        new_expanded = []
        for comp in expanded_components:
            if var not in comp and f'!{var}' not in comp:
                # Split the component into two: one with the variable and one with its negation
                new_expanded.append(sorted(comp + [var], key=lambda x: variables.index(x.strip('!'))))
                new_expanded.append(sorted(comp + [f'!{var}'], key=lambda x: variables.index(x.strip('!'))))
            else:
                new_expanded.append(comp)  # Keep it as is if the variable is already present
        expanded_components = new_expanded

    return expanded_components

def truth_table_order_key(component, variables):
    """
    Converts a component to a binary string based on the truth table order.
    """
    binary_string = ''
    for var in variables:
        if f'!{var}' in component:
            binary_string += '0'  # Negated variable
        elif var in component:
            binary_string += '1'  # Non-negated variable
        else:
            binary_string += '0'  # Missing variable defaults to 0 for POS

    # Convert the binary string to an integer for sorting
    return int(binary_string, 2)

def canonicalPOS(expr, variables):
    """
    Converts a POS expression to its canonical POS form.
    """
    # Step 1: Extract components first
    components = extract_components(expr, variables)
    
    # Step 2: Expand components to include all variables
    canonical_expr = set()

    for component in components:
        expanded_components = expand_component(component, variables)
        for expanded in expanded_components:
            canonical_expr.add(tuple(expanded))  # Use tuple to store in set

    # Step 3: Sort the components based on the truth table order
    sorted_components = sorted(canonical_expr, key=lambda x: truth_table_order_key(x, variables), reverse=True)

    # Step 4: Convert the sorted components into the final canonical form
    canonical_expr_str = ' * '.join(['(' + ' + '.join(comp) + ')' for comp in sorted_components])

    return canonical_expr_str

# Example usage (test 1)
print("Test 1: Canonical POS Expression")
variables = ['p', 'q', 'r', 's']
expr = "(q + p) * !r * (r + p + !s)"
canonical_expr = canonicalPOS(expr, variables)
print("Canonical POS Expression:", canonical_expr)
print()

# Example usage (test 2)
print("Test 2: From Wolfram Cloud POS expr to canonical POS in py") 
expr = "(!A||!B||C)&&(!A||!B||D)&&(A||!C||!D)&&(A||C||D)&&(B||!C||!D)"
variables = ['A', 'B', 'C', 'D']
expr = toPY(expr)
print("Converting it to py:", expr)
canonical_expr = canonicalPOS(expr, variables)
print("Canonical POS Expression:", canonical_expr)
print()

exprWAL = toWAL(canonical_expr)
print("Converting it to WAL:", exprWAL)

exprLatex = PYtoLatexCode(expr)
print("Converting it to latex code:", exprLatex)