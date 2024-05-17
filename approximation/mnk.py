import numpy as np

def mnk(x: np.array, y: np.array, higher_degree=1):
    m = higher_degree + 1

    b = np.empty(m)  # b
    g = np.empty((m, m))  # Г

    # заполняем b = (P^T)*P
    for j in range(m):
        b[j] = np.sum(y * x ** j)

    # заполняем Г = P*P
    for j in range(m):
        for k in range(m):
            g[j][k] = sum(x ** (k + j))

    best_coeffs = np.linalg.solve(g, b)

    def f(px):
        py = 0
        for i in range(m):
            py += best_coeffs[i] * px ** i
        return py

    return f, best_coeffs