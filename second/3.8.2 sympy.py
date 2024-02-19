import numpy as np
import sympy as sp


def gauss_elimination_sympy(A: np.array, b: sp.Matrix):
    n = A.shape[0]
    x = sp.Matrix([0] * n)

    # прямой ход
    for i in range(n):

        # ищем максимальный коэффициент среди уравнений с неизвестными x и берем его индекс
        A_slice = A[i:][:]
        max_element_row_index = np.unravel_index(np.argmax(A_slice), A_slice.shape)[0] + i

        # меняем местами i-ое и max_element_row_index-ое уравнения
        if max_element_row_index != i:
            A[[i, max_element_row_index]] = A[[max_element_row_index, i]]  # синтаксис numpy
            b.elementary_row_op('n<->m', row1=i, row2=max_element_row_index)  # синтаксис sympy

        # убираем коэффициенты при x
        for j in range(i + 1, n):
            mu = A[j][i] / A[i][i]
            A[j] -= mu * A[i]
            b[j] -= mu * b[i]

    # обратный ход
    for m in range(n - 1, -1, -1):
        numerator = b[m]
        for l in range(m, n):
            numerator -= A[m][l] * x[l]
        denominator = A[m][m]
        x[m] = numerator / denominator
        x[m] = (b[m] - np.dot(A[m, m + 1:], x[m + 1:])) / A[m, m]

    return sp.sympify(x)


n = 40
M = 2
q = 1.001 - 2 * M / 1000
X = sp.Symbol('x')

# заполним матрицу A и вектор b
A = np.ndarray((n, n))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            A[i - 1][j - 1] = q ** (i + j) + 0.1 * (j - i)
        else:
            A[i - 1][j - 1] = (q - 1) ** (i + j)
b = sp.Matrix([sp.Abs(X - n / 10) * i * sp.sin(X) for i in range(1, n + 1)])

my_x = gauss_elimination_sympy(A, b)
sp_x = sp.simplify(sp.Matrix(A.tolist()).solve(b))

print("Решение системы уравнений Ax=b методом Гаусса:", my_x)
print("Решение системы уравнений Ax=b методом Гаусса:", sp_x)
