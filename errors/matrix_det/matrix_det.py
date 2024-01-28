import numpy as np
from itertools import product


def is_inverse_matrix_exist(matrix: np.ndarray):
    matrix_det = np.linalg.det(matrix)
    print(f'Определитель без погрешности {matrix_det}')
    print()


def is_inverse_matrix_exist_with_error(matrix: np.ndarray, delta: float):
    metrix_dets = []
    for sign in list(product([-1, 1], repeat=9)):
        new_matrix = matrix * (1 + np.array(sign).reshape(3, 3) * delta)
        metrix_dets.append(np.linalg.det(new_matrix))

    min_det = np.min(metrix_dets)
    max_det = np.max(metrix_dets)
    print(f'Минимальное значение определителя = {min_det}')
    print(f'Максимальное значение определителя = {max_det}')

    if min_det < 0 < max_det:
        print(f"При относительной погрешности {delta} определитель может обратиться в 0")
    else:
        print(f"При относительной погрешности {delta} определитель не может обратиться в 0")
    print()


matrix = np.array([[30, 34, 19],
                   [31.4, 35.4, 20],
                   [24, 28, 13]])

is_inverse_matrix_exist(matrix)
is_inverse_matrix_exist_with_error(matrix, 0.05)
is_inverse_matrix_exist_with_error(matrix, 0.1)
