import sympy as sp

def integral_indefinida():
    x = sp.Symbol('x')
    integral = sp.integrate(x**2, x)
    print(integral)  # Salida: x**3/3

def integral_definida():
    integral_def = sp.integrate(x**2, (x, 0, 2))
    print(integral_def)  # Salida: 8/3