import numpy as np

A = np.array([[52, 20, 25],
              [30, 50, 20],
              [18, 30, 55]])

B = np.array([4800, 5810, 5690])

# Para la inversa de la matriz
A_inv = np.linalg.inv(A)

# Multiplicando las matrices
X = np.dot(A_inv, B)

# Imprimir el resultado
for i, x in enumerate(X, 1):
    print(f"Cantidad a transportar desde la cantera {i}: {x:.2f} metros cúbicos")
