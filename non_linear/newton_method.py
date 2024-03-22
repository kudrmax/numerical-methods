import numpy as np
import sympy as sp
import scipy
import matplotlib.pyplot as plt

x1 = sp.Symbol('x1')
x2 = sp.Symbol('x2')

f1 = sp.cos(x1 + x2) + 2 * x2
f2 = x1 + sp.sin(x2) - 0.6

F = sp.Matrix([f1, f2])


def eq(vars):
    x1, x2 = vars
    f1 = sp.cos(x1 + x2) + 2 * x2
    f2 = x1 + sp.sin(x2) - 0.6
    return [f1, f2]


def calculate_root(F, X_num: np.array, eps: float = 0.000001) -> np.array:
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


X1 = np.array([2.5, 0.1])
X2 = np.array([-4.5, -0.1])

X1_my, count1 = calculate_root(F, X1, 0.000001)
X2_my, count2 = calculate_root(F, X2, 0.000001)


X1_scipy = scipy.optimize.fsolve(eq, X1)
X2_scipy = scipy.optimize.fsolve(eq, X2)

print(f'{X1_my = }')
print(f'Количество итераций: {count1}')
print()

print(f'{X1_my = }')
print(f'Количество итераций: {count1}')
print()

print(f'{X1_scipy = }')
print(f'{X2_scipy = }')

plt.plot(*X1_my, marker='o', color='green', ls='')
x1, x2 = np.meshgrid(np.arange(-10, 10, 0.05), np.arange(-10, 10, 0.05))
plt.contour(x1, x2, np.cos(x1 + x2) + 2 * x2, [0], colors=['red'])
plt.contour(x1, x2, x1 + np.sin(x2) - 0.6, [0], colors=['blue'])
plt.savefig('nonlinear_newton_with_point.png', dpi=300)
plt.show()