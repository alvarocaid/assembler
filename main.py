def expand_component(component, variables):
  """
  Expands a single component to include all variables in the given domain,
  adding parentheses to maintain proper expression format.
  """
  if len(variables) == 0:
      return [f"({component})"]  # Base case: Enclose in parentheses

  print(f"{variables[0]}: {variables[1:]}")
  current_var = variables[0]
  remaining_vars = variables[1:]

  # If the current variable or its negation is in the component, proceed with the next variable.
  if current_var in component or f'!{current_var}' in component:
      print(f"Skipping {current_var} and !{current_var} in {component}")
      return expand_component(component, remaining_vars)
  print(f"Expanding {component} with {current_var} and !{current_var}")
  print()
  # Otherwise, split the component into two: one with the variable and one with its negation.
  expanded_with_var = expand_component(f"{component} + {current_var}", remaining_vars)
  expanded_with_not_var = expand_component(f"{component} + !{current_var}", remaining_vars)

  return expanded_with_var + expanded_with_not_var

def canonicalPOS(expr, variables):
  """
  Converts a POS expression to its canonical POS form.
  """
  # Remove outer parentheses and split the expression by '*'
  components = expr.replace('(', '').replace(')', '').split('*')
  canonical_expr = set()

  for component in components:
      expanded_components = expand_component(component.strip(), variables)
      canonical_expr.update(expanded_components)

  # Convert the canonical_expr set to a string in canonical form
  canonical_expr_str = ' * '.join(sorted(canonical_expr))

  return canonical_expr_str

# Example usage
variables = ['p', 'q', 'r']
expr = "(p + q + r)* r"
canonical_expr = canonicalPOS(expr, variables)
print("Canonical POS Expression:", canonical_expr)
