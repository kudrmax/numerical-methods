import numpy as np
import sympy as sp
import os

output_file = "3.8.2"


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

        # избавляемся от коэффициентов при x
        for j in range(i + 1, n):
            mu = A[j][i] / A[i][i]
            A[j] -= mu * A[i]
            b[j] -= mu * b[i]

    # обратный ход
    for m in range(n - 1, -1, -1):
        numerator = b[m]  # числитель
        for l in range(m + 1, n):
            numerator -= A[m][l] * x[l]
        denominator = A[m][m]  # знаменатель
        x[m] = numerator / denominator

    return sp.sympify(x)


# os.remove(output_file + '.txt')
with open(output_file + '.txt', "w") as f:
    # зададим константы
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

    # решим систему
    my_z = gauss_elimination_sympy(A, b)
    sp_z = sp.simplify(sp.Matrix(A.tolist()).solve(b))
    print("Решение системы посчитанное через мою функцию:\n", my_z, file=f)
    print("Решение системы посчитанное через sympy:\n", sp_z, file=f)
    print(file=f)

    # вычислим y
    my_y = 0
    sp_y = 0
    for i in range(len(my_z)):
        my_y += my_z[i]
        sp_y += sp_z[i]
    print("Значение 'y' посчитанное через мою функцию:", my_y, file=f)
    print("Значение 'y' посчитанное через sympy:", sp_y, file=f)

    # построим график
    graph = sp.plot(my_y, sp_y, (X, -5, 5), line_color='red', dpi=300)
    backend = graph.backend(graph)
    backend.process_series()
    backend.fig.savefig(output_file + '.png', dpi=300)
    backend.show()
