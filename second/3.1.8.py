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

    # найдем вектор d
    delta = 0.01
    d = np.empty(n)
    for i in range(n):
        bi = b.copy()
        bi[i] += delta
        xi = np.linalg.solve(A, bi)
        d[i] = np.linalg.norm(x - xi, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
    print(f"{d = }", file=f)

    # найдем что оказывает наибольшее влияние на погрешность
    d_max = d.max()
    d_max_index = list(d).index(d_max)
    print(f'{d_max = } with {d_max_index = }', file=f)

    # построим гистограмму
    plt.bar(list(range(0, len(d))), d)
    plt.savefig('3.1.8.png', dpi=300)
    plt.show()

with open(output_file_path, "r") as f:
    print(f.read())
