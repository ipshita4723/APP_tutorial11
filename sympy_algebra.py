from sympy import *

x = symbols('x')

expr = (x + 2)*(x + 3)

print("Original Expression =", expr)

print("Expanded Form =", expand(expr))

print("Factored Form =", factor(expand(expr)))

expr2 = (x**2 + 2*x)/x

print("Simplified Form =", simplify(expr2))

equation = Eq(x**2 - 5*x + 6, 0)

print("Roots =", solve(equation, x))
