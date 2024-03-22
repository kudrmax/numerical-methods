import numpy as np
import matplotlib.pyplot as plt


def relax(A, b, x0, eps, w):
    B = np.empty(A.shape, dtype=float)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B[i, j] = - A[i, j] / A[i, i] if i != j else 0

    c = np.empty(b.shape, dtype=float)
    for i in range(c.shape[0]):
        c[i] = b[i] / A[i, i]

    B1 = np.zeros(B.shape)
    B2 = np.zeros(B.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if j < i:
                B1[i, j] = B[i, j]
            if j > i:
                B2[i, j] = B[i, j]

    x = x0
    count = 0
    while True:
        count += 1
        x_new = np.zeros(x.shape, dtype=float)
        for i in range(B.shape[0]):  # x_new = B1 @ x_new + B2 @ x + c
            x_new[i] = np.sum(B[i][:i] * x_new[:i]) + np.sum(B[i][i:] * x[i:]) + c[i]
            x_new[i] = w * x_new[i] + (1 - w) * x[i]
        norma = np.linalg.norm(x_new - x)
        x = x_new

        eps_new = ((1 - np.linalg.norm(B, ord=np.inf)) * eps) / np.linalg.norm(B2, ord=np.inf)
        if norma < eps_new:
            break
    return x, count


A = np.array([[3.5,-1, 0.9, 0.2, 0.1],
              [-1, 7.3, 2, 0.3, 2],
              [0.9, 2, 4.9, -0.1, 0.2],
              [0.2, 0.3, -0.1, 5, 1.2],
              [0.1, 2, 0.2, 1.2, 7]])

b = np.array([1.0, 2, 3, 4, 5])

x_true = np.linalg.solve(A, b)

w_list = []
count_list = []
x_list = []
for w in np.arange(0.1, 1.9, 0.01):
    w = round(w, 2)
    x_relax, count = relax(A, b, np.zeros(b.shape[0]), 0.00001, w)
    x_list.append(x_relax)
    w_list.append(w)
    count_list.append(count)

best_w = None
best_count = np.inf
best_x = None
for w, count, x in zip(w_list, count_list, x_list):
    if count < best_count:
        best_count = count
        best_w = w
        best_x = x

print(f'Решение методом Гаусса: {x_true}')
print('Решение иетодом релаксации при минимальном количестве итераций:')
print(f'Решение системы методом релаксации: {best_x}')
print(f'Количество итераций: {best_count}')
print(f'Параметр w: {best_w}')

plt.plot(w_list, count_list)
plt.savefig('w_count.png', dpi=300)
plt.show()
