import numpy as np
import sympy as sp

N = 2
a1 = 8.5 - N * 0.25
a2 = 2.3 + N * 0.3
a3 = 4.0 + N * 0.1

P_list = np.array([
    [16, 5.8, 11.879],
    [8.485, 5.328, 8.91],
    [15.0, 3.139, 5.25],
])

x1, x2, x3 = sp.symbols('x1 x2 x3')
phi, teta = sp.symbols('alpha teta')
Angle = np.array([phi, teta])


def from_angles_to_x(Angle):
    phi, teta = Angle
    x1 = a1 * sp.sin(phi) * sp.sin(teta)
    x2 = a2 * sp.cos(phi) * sp.sin(teta)
    x3 = a3 * sp.cos(phi)
    return np.array([x1, x2, x3])


X = from_angles_to_x(Angle)

def find_min_newton(H, X0, X_sym):
    Angle = X_sym
    X_num = X0

    g = sp.Matrix([H.diff(angle) for angle in Angle])
    G = sp.Matrix([[H.diff(angle1).diff(angle2) for angle1 in Angle] for angle2 in Angle])

    eps = 0.01
    count_iteration = 0
    while True:
        g_num = np.array(g.subs(zip(Angle, X_num)), dtype=float)
        G_num = np.array(G.subs(zip(Angle, X_num)), dtype=float)
        # p_num = np.linalg.solve(G_num, -g_num).flatten()
        p_num = (np.linalg.inv(G_num) @ (-g_num)).flatten()
        alpha = 0.5
        X_new = X_num + alpha * p_num
        if np.linalg.norm(X_new - X_num) < eps:
            break
        X_num = X_new

        dist = sp.Expr(H).subs(zip(Angle, X_num))
        print(dist)

        count_iteration += 1

    return X_num, count_iteration

for P in P_list:

    H = sum((X - P) ** 2)

    # for
    X_num = np.array([100, 0], dtype=float)

    X_num, count = find_min_newton(H, X_num, Angle)


    # dist = sp.Expr(H).subs(zip(Angle, X_num))
    # print(f'{dist = }')

    # print(f'{P = }')
    # print(f'{X_num = }')
    # print(f'{count_iteration = }')

    print()


# x1, x2 = sp.symbols('x1 x2')
# Angle = np.array([x1, x2])
# H = x1 ** 2 + 10 * (x2 - sp.sin(x1)) ** 2
# X_num, count = find_min_newton(H, np.array([10, 10]), Angle)
# print(X_num, count)