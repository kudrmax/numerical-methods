import numpy as np
import matplotlib.pyplot as plt
import os

output_file_path = "3.1.8.txt"

n = 6
N = 8

os.remove(output_file_path)
with open(output_file_path, "a") as f:

    # заполним матрицу A
    A = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            c = 0.1 * N * (i + 1) * (j + 1)
            A[i][j] = 1 / np.sqrt(c ** 2 + 0.58 * c)

    # заполним вектор b
    b = np.full(n, N, dtype=float)

    # найдем решение через встроенную функцию
    x = np.linalg.solve(A, b)
    print(f"{x = }", file=f)

    # найдем число обусловленности через встроенную функцию
    A_cond = np.linalg.cond(A, np.inf)
    print(f"{A_cond = }", file=f)

    # найдем вектор множества векторов b
    delta = 0.05
    b_error_set = []
    for i in range(n):
        b_error = b.copy()
        b_error[i] += delta
        b_error_set.append(b_error)

    # найдем вектор d
    d = np.empty(n)
    for i in range(n):
        b_error = b_error_set[i]
        x_error = np.linalg.solve(A, b_error)
        d[i] = np.linalg.norm(x - x_error, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
    print(f"{d = }", file=f)

    # найдем что оказывает наибольшее влияние на погрешность
    d_max = d.max()
    d_max_index = list(d).index(d_max)
    print(f'{d_max = } with {d_max_index = }', file=f)

    # построим гистограмму
    plt.bar(range(n), d)
    plt.savefig('3.1.8.png', dpi=300)
    plt.show()

    print(f"delta_rel_x_error:", file=f)
    for i in range(n):
        b_error = b_error_set[i]
        # delta_rel_b_old = np.linalg.norm(b - b_error, ord=np.inf) / np.linalg.norm(b, ord=np.inf)
        delta_rel_b = np.abs(delta) / np.linalg.norm(b, ord=np.inf)
        # @todo вывести теоретически
        delta_rel_x_error = A_cond * delta_rel_b
        print(f"практически: {d[i]},\tтеоритически: {delta_rel_x_error}", file=f)

with open(output_file_path, "r") as f:
    print(f.read())
