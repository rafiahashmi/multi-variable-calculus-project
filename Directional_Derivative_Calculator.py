# Step 1: User input for function and partial derivatives
import math

import sympy as sp

x, y = sp.symbols('x y')

expr = input("Enter your function: ")   # user se function input
f = sp.sympify(expr)                               # string ko SymPy expression me convert karega

fx = sp.diff(f, x)   # ∂f/∂x
fy = sp.diff(f, y)   # ∂f/∂y

print("\nYour function f(x, y) =", f)
print("∂f/∂x =", fx)
print("∂f/∂y =", fy)

# Step 2: Evaluate partial derivatives at a specific point
x0, y0 = map(float, input("Enter point p (x0 and y0) (space separated): ").split())

# substitute values in fx and fy
fx_val = fx.subs({x: x0, y: y0})
fy_val = fy.subs({x: x0, y: y0})

print(f"\nAt point ({x0}, {y0}):")
print(f"∂f/∂x = {(fx_val)}")
print(f"∂f/∂y = {(fy_val)}")

print("\nEnter direction vector components: ")
a , b = map (float , input ("enter points a and b ").split())
mag = sp.sqrt(a**2+b**2)
u1 = a/mag
u2 = b/mag

Duf = (fx_val*u1 + fy_val*u2)
print(f"\nDirectional Derivative Duf = {(Duf)}")
