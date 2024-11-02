import numpy as np

from lab7.tridiagonal_matrix_algorithm import tridiagonal_matrix_algorithm


def get_coeffs(g1, g2, f, x, h, n):
    a = np.ones(n) / h ** 2 - g1(x) / (2 * h)
    b = -np.full(n, 2) / h ** 2 + g2(x)
    c = np.ones(n) / h ** 2 + g1(x) / (2 * h)
    d = f(x)
    return a, b, c, d


def get_solution(g1, g2, f, apply_boundary_conditions, n, x_left, x_right):
    """
    Решение уравнения вида u''(x) + g1(x) * u'(x) + g2(x) * u(x) = f(x)

    Parameters
    ----------
    g1 - функция из уравнения
    g2 - функция из уравнения
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
    a, b, c, d = get_coeffs(g1, g2, f, x, h, n)

    # применение граничных условий
    apply_boundary_conditions(a, b, c, d, h)

    # использование метода прогонки
    u = tridiagonal_matrix_algorithm(a, b, c, d)

    return u, x
