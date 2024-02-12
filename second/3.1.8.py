import numpy as np

n = 6
N = 8

# заполним матрицу A
A = np.empty((n, n))
for i in range(n):
    for j in range(n):
        c = 0.1 * N * (i + 1) * (j + 1)
        A[i][j] = 1 / np.sqrt(c ** 2 + 0.58 * c)

# заполним веторк b
b = np.full(n, N, dtype=float)

# найдем решение через встроенную функцию
x = np.linalg.solve(A, b)
print(f"{x = }")

# найдем число обусловленности через встроенную функцию
A_cond = np.linalg.cond(A, np.inf)
print(f"{A_cond = }")

# найдем вектор d
delta = 0.01
d = np.empty(n)
for i in range(n):
    bi = b.copy()
    bi[i] += delta
    xi = np.linalg.solve(A, bi)
    d[i] = np.linalg.norm(x - xi, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
print(f"{d = }")
