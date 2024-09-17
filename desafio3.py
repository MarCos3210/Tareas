import numpy as np

# Definir la matriz de coeficientes y el vector de resultados
A = np.array([[52, 20, 25],
              [30, 50, 20],
              [18, 30, 55]])

B = np.array([4800, 5810, 5690])

# Definir la función para el método de Jacobi
def jacobi(A, B, tol=0.005, max_iterations=1000):
    # Descomponer A en D, L y U
    D = np.diag(np.diag(A))  # Matriz diagonal
    L = np.tril(A, -1)       # Matriz triangular inferior estricta
    U = np.triu(A, 1)        # Matriz triangular superior estricta

    # Inicializar la primera aproximación (puede ser un vector de ceros)
    x = np.zeros_like(B, dtype=np.float64)
    
    # Calcular la matriz de Jacobi
    D_inv = np.linalg.inv(D)
    T_jacobi = -np.dot(D_inv, (L + U))
    C_jacobi = np.dot(D_inv, B)

    # Cálculo de los alfas (valores propios de la matriz de iteración)
    alfas = np.linalg.eigvals(T_jacobi)
    alfa_max = max(abs(alfas))
    
    print(f"Máximo alfa (valor propio) de la matriz de Jacobi: {alfa_max:.4f}")

    # Verificar si el método convergerá
    if alfa_max >= 1:
        print("El método de Jacobi no convergerá porque el máximo valor propio es >= 1.")
        return None

    # Iteración de Jacobi
    iter_count = 0
    while iter_count < max_iterations:
        x_new = np.dot(T_jacobi, x) + C_jacobi

        # Verificar la convergencia (si la diferencia es menor que la tolerancia)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break

        # Actualizar la solución
        x = x_new
        iter_count += 1

    return x, iter_count

# Ejecutar el método de Jacobi
solucion, iteraciones = jacobi(A, B)

if solucion is not None:
    print(f"Solución en {iteraciones} iteraciones:")
    for i, valor in enumerate(solucion, 1):
        print(f"Cantidad a transportar desde la cantera {i}: {valor:.2f} metros cúbicos")
