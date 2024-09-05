import sympy as sp
import math as mt

m = sp.symbols('m')
funcion = sp.cos(m)

x0 = mt.pi/4
x1 = mt.pi/3

valor_x0 = funcion.subs(m, x0)
valor_x1 = funcion.subs(m, x1)
h = x1 - x0

ef = 1
i = 1

# Ciclo de iteraciones derivada
while ef>0.0005:
    
    derivada = sp.diff(funcion, m)

    print(derivada)
    
    # Evaluar la derivada
    f_derivado = derivada.subs(m, x0)

    x1 = valor_x0 + f_derivado * h**i / mt.factorial(i)

    ef = abs(f_derivado*h**i / mt.factorial(i))

    print('x1',x1)
    print('f derivado',f_derivado)
    print('error',ef)

    valor_x0 = x1
    funcion = derivada
    i = i + 1

