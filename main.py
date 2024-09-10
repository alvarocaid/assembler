import re

def extract_components(expr, variables):
    """
    Extracts components from the POS expression, preserving variable order as per 'variables'.
    Returns a list of lists, where each inner list represents a component.
    """
    # Replace + with a space to simplify splitting components
    expr = expr.replace(' ', '').replace('+', ' + ').replace('*', ' * ')
    
    # Split the expression by '*' to get each clause
    clauses = [clause.strip() for clause in expr.split('*')]
    
    components = []
    
    # For each clause, split by '+' and gather variables
    for clause in clauses:
        clause_components = []
        clause_vars = re.split(r'\s*\+\s*', clause)
        # Now organize the variables based on the given order in 'variables'
        for var in variables:
            # Add negated variable if it's present, else add the regular variable
            if f'!{var}' in clause_vars:
                clause_components.append(f'!{var}')
            elif var in clause_vars:
                clause_components.append(var)
        
        components.append(tuple(clause_components))  # Use tuple for immutability in set later
    
    return components

def expand_component(component, variables):
    """
    Expands a single component to include all variables in the given domain,
    adding parentheses to maintain proper expression format.
    """
    if len(variables) == 0:
        return [f"({component})"]  # Base case: Enclose in parentheses

    current_var = variables[0]
    remaining_vars = variables[1:]

    # If the current variable or its negation is in the component, proceed with the next variable.
    if current_var in component or f'!{current_var}' in component:
        return expand_component(component, remaining_vars)

    # Otherwise, split the component into two: one with the variable and one with its negation.
    expanded_with_var = expand_component(f"{component} + {current_var}", remaining_vars)
    expanded_with_not_var = expand_component(f"{component} + !{current_var}", remaining_vars)

    return expanded_with_var + expanded_with_not_var

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
    # Extract components first
    components = extract_components(expr, variables)
    
    # Use a set to store canonical form components
    canonical_expr = set()

    for component in components:
        expanded_components = expand_component(' + '.join(component), variables)
        canonical_expr.update(expanded_components)

    # Sort the components based on the truth table order
    sorted_components = sorted(canonical_expr, key=lambda x: truth_table_order_key(x, variables), reverse=True)

    # Convert the sorted components set to a string in canonical form
    canonical_expr_str = ' * '.join(sorted_components)

    return canonical_expr_str

# Example usage
variables = ['p', 'q', 'r']
expr = "p + q + !r * r"
components = extract_components(expr, variables)
print("Extracted Components:", components)

canonical_expr = canonicalPOS(expr, variables)
print("Canonical POS Expression:", canonical_expr)
