import numpy as np
import sympy as sp

x1 = sp.Symbol('x1')
x2 = sp.Symbol('x2')

f1 = sp.cos(x1 + x2) + 2 * x2
f2 = x1 + sp.sin(x2) - 0.6

F = sp.Matrix([f1, f2])


def calculate_root(F, X_num: np.array, eps: float = 1e-6) -> np.array:
    iter_count = 0
    jacobian = F.jacobian([x1, x2]).inv() * F
    while True:
        jacobian_num = jacobian.subs([(x1, X_num[0]), (x2, X_num[1])])
        X_num -= np.array(jacobian_num, dtype=float).flatten()
        iter_count += 1
        norm = np.linalg.norm(np.array(F.subs([(x1, X_num[0]), (x2, X_num[1])]), dtype=float).flatten())
        if norm < eps:
            break
    return X_num, iter_count


print(calculate_root(F, np.array([1.0, -10.9]), 0.000001))
