import numpy as np


def gauss_elimination_number(A: np.ndarray, b: np.array) -> np.array:
    n = A.shape[0]
    x = np.empty(n, dtype=float)

    # храним индексы иксов, чтобы сделать обратный ход
    col_indexes = np.empty(n, dtype=int)

    # прямой ход
    for i in range(n):

        # ищем максимальный коэффициент среди уравнений с неизвестными x и берем его индекс
        A_slice = A[i:][:]
        max_element_row_index = np.unravel_index(np.argmax(A_slice), A_slice.shape)[0] + i
        max_element_col_index = np.unravel_index(np.argmax(A_slice), A_slice.shape)[1]
        col_indexes[i] = max_element_col_index

        # меняем местами i-ое и max_element_row_index-ое уравнения
        if max_element_row_index != i:
            A[[i, max_element_row_index]] = A[[max_element_row_index, i]]
            b[[i, max_element_row_index]] = b[[max_element_row_index, i]]

        # убираем коэффициенты при x
        for j in range(i + 1, n):
            mu = A[j][max_element_col_index] / A[i][max_element_col_index]
            A[j] -= mu * A[i]
            b[j] -= mu * b[i]

    # обратный ход
    for k in range(col_indexes.shape[0]):
        m = col_indexes[-1 - k]  # идем в обратном порядке по идексам, которые сохранили
        numerator = b[m]  # числитель
        for l in range(m + 1, n):
            numerator -= A[m][l] * x[l]
        denominator = A[m][m]  # знаменатель
        x[m] = numerator / denominator

    return x


A = np.array([[2.0, 1.0, -1.0],
              [-3.0, -1.0, 2.0],
              [-2.0, 1.0, 2.0]])
b = np.array([8.0, -11.0, -3.0])

my_x = gauss_elimination_number(A, b)
np_x = np.linalg.solve(A, b)

print("Решение системы уравнений Ax=b методом Гаусса:", my_x)
print("Решение системы уравнений Ax=b методом Гаусса:", np_x)
print(f"Решения через np.solve и мое решения {'совпадают' if np.allclose(my_x, np_x) else 'не совпадают'}")
