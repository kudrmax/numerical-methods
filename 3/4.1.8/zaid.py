import numpy as np


def zaid(A, b, x0, n):
    B = np.empty(A.shape, dtype=float)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B[i, j] = - A[i, j] / A[i, i] if i != j else 0

    c = np.empty(b.shape, dtype=float)
    for i in range(c.shape[0]):
        c[i] = b[i] / A[i, i]

    # B1 = np.zeros(B.shape)
    # B2 = np.zeros(B.shape)
    # for i in range(A.shape[0]):
    #     for j in range(A.shape[1]):
    #         if j < i:
    #             B1[i, j] = B[i, j]
    #         if j > i:
    #             B2[i, j] = B[i, j]

    x = x0
    for _ in range(n):
        x_new = np.zeros(x.shape, dtype=float)
        for i in range(B.shape[0]):  # x_new = B1 @ x_new + B2 @ x + c
            x_new[i] = np.sum(B[i][:i] * x_new[:i]) + np.sum(B[i][i:] * x[i:]) + c[i]
        x = x_new
    return x

def relax(A, b, x0, n, w):
    B = np.empty(A.shape, dtype=float)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B[i, j] = - A[i, j] / A[i, i] if i != j else 0

    c = np.empty(b.shape, dtype=float)
    for i in range(c.shape[0]):
        c[i] = b[i] / A[i, i]

    # B1 = np.zeros(B.shape)
    # B2 = np.zeros(B.shape)
    # for i in range(A.shape[0]):
    #     for j in range(A.shape[1]):
    #         if j < i:
    #             B1[i, j] = B[i, j]
    #         if j > i:
    #             B2[i, j] = B[i, j]

    x = x0
    for _ in range(n):
        x_new = np.zeros(x.shape, dtype=float)
        for i in range(B.shape[0]):  # x_new = B1 @ x_new + B2 @ x + c
            x_new[i] = np.sum(B[i][:i] * x_new[:i]) + np.sum(B[i][i:] * x[i:]) + c[i]
            x_new[i] = w * x_new[i] + (1 - w) * x[i]
        x = x_new
    return x


A = np.array([[118.8, -14, -5, -89.1],
              [-59.4, 194, 5, 128.7],
              [148.5, 12, -310, 148.5],
              [0, 18.5, 90, -108.9]])

b = np.array([92.5, -340.1, -898, 184.1])

x_true = np.linalg.solve(A, b)
x_zaid = zaid(A, b, np.zeros(b.shape[0]), 10)
x_relax = relax(A, b, np.zeros(b.shape[0]), 10, 1.25)

print(f'{x_true = }')
print(f'{x_zaid = }')
print(f'{x_relax = }')
