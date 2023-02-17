import numpy as np
import sympy as sp
import os
os.system('cls')

x = sp.symbols('x')
tr = 0.1017*x**2 - 5.527*x + 80.89
td = -0.0228*x**2 + 0.03431*x + 42.27
equation = sp.Eq(td, tr)
#print(sp.solveset(equation)) # sp.solveset() = devolve os valores de 'x' nas raízes da equação
solutions = sp.solveset(equation)
for i in solutions:
    print(f'V = {i} m/s, T = {td.subs(x, i)}')
