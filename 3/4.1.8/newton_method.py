import numpy as np
#
# def root(f, initial: np.array, eps: float = 1e-6) -> np.array:
#     x = initial.astype(np.double)
#     iter_cnt = 0
#     f_cnt = len(f(initial))
#     while np.linalg.norm(f(x)) > eps:
#         x -= np.linalg.inv(jacobian(f, x, f_cnt)).dot(f(x))
#         iter_cnt += 1
#     return x, iter_cnt

# def jacobian(f, x: np.array, f_cnt: int, eps: float = 1e-5) -> np.array:
#     jac = np.zeros((f_cnt, len(x)), dtype=np.double)
#
#     for i in range(len(x)):
#         delta = np.zeros(len(x))
#         delta[i] += eps
#         jac[:, i] = (f(x + delta) - f(x - delta)) / (eps * 2)
#     return jac


import sympy as sp

x1 = sp.Symbol('x1')
x2 = sp.Symbol('x2')

f1 = sp.cos(x1 + x2) + 2 * x2
f2 = x1 + sp.sin(x2) - 0.6

X = sp.Matrix([x1, x2])
F = sp.Matrix([f1, f2])

# print(F.jacobian([x1, x2]))


def root(F, X_num: np.array, eps: float = 1e-6) -> np.array:
    iter_count = 0
    while True:
        j = F.jacobian([x1, x2])
        j = j.inv()
        j = (j * F).T
        j_num = j.subs([(x1, X_num[0]), (x2, X_num[1])])
        j_num = np.array(j_num)
        j_num = j_num[0]
        X_num = X_num - j_num
        # X_num -= j.subs(X_num)
        X_num = np.array(X_num, dtype=float)
        iter_count += 1
        # if iter_count > 10:
        #     break
        norma = np.linalg.norm(X_num)
        if norma > eps:
            break
    return X_num, iter_count


print(root(F, np.array([1.0, -0.5]), 0.0001))
print(np.array([1, 2]), 5)

a = sp.Matrix([[-sp.sin(x1 + x2), 2 - sp.sin(x1 + x2)], [1, sp.cos(x2)]])
# a = a.inv()