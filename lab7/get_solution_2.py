import numpy as np

from lab7.tridiagonal_matrix_algorithm import tridiagonal_matrix_algorithm


def get_coeffs(k, q, f, x, h, n):
    a, b, c, d = np.empty(n), np.empty(n), np.empty(n), np.empty(n)
    for i in range(1, n - 1):
        k_half_right = (k(x[i]) + k(x[i + 1])) / 2
        k_half_left = (k(x[i]) + k(x[i - 1])) / 2
        a[i] = -k_half_left / h ** 2
        b[i] = (k_half_left + k_half_right) / h ** 2 + q(x[i])
        c[i] = -k_half_right / h ** 2
    d = f(x)
    return a, b, c, d


def get_solution(k, q, f, apply_boundary_conditions, n, x_left, x_right):
    """
    Решение уравнения вида ДОПИСАТЬ

    Parameters
    ----------
    k - функция из уравнения
    q - функция из уравнения
    f - функция из уравнения
    gran_usl - функция, которая задает граничные условия
    n - количество узлов сетки
    x_left - левая граница
    x_right - правая граница
    """

    # подготовка
    x = np.linspace(x_left, x_right, n)
    h = (x_right - x_left) / (n - 1)

    # вычисление коэффициентов матрицы
    a, b, c, d = get_coeffs(k, q, f, x, h, n)

    # применение граничных условий
    apply_boundary_conditions(a, b, c, d, h)

    # использование метода прогонки
    u = tridiagonal_matrix_algorithm(a, b, c, d)
    return u, x
