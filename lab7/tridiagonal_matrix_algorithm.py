import numpy as np


def tridiagonal_matrix_algorithm(a, b, c, d):
    """
    Метод прогонки

    a - нижняя диагональ (1 <= i <= n-1)
    b - главная диагональ (0 <= i <= n-1)
    c - верхняя диагональ (0 <= i <= n-2)
    d - правая часть уравнения
    """
    n = len(d)
    alpha = np.zeros(n)
    beta = np.zeros(n)

    # прямой ход
    alpha[0] = -c[0] / b[0]
    beta[0] = d[0] / b[0]
    for i in range(1, n):
        gamma = b[i] + a[i] * alpha[i - 1]
        alpha[i] = -c[i] / gamma if i < n - 1 else 0
        beta[i] = (d[i] - a[i] * beta[i - 1]) / gamma

    # обратный ход
    u = np.zeros(n)
    u[-1] = beta[-1]
    for i in range(n - 2, -1, -1):
        u[i] = alpha[i] * u[i + 1] + beta[i]

    return u