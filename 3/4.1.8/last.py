import numpy as np
import sympy as sp

N = 2
a1 = 8.5 - N * 0.25
a2 = 2.3 + N * 0.3
a3 = 4.0 + N * 0.1

x1 = sp.Symbol('x1')
x2 = sp.Symbol('x2')
x3 = sp.Symbol('x3')

S = (x1 / a1) ** 2 + (x2 / a2) ** 2 + (x3 / a3) ** 2 - 1

P_list = np.array([
    [16, 5.8, 11.879],
    [8.485, 5.328, 8.91],
    [15.0, 3.139, 5.25],
])

P = P_list[0]

X = np.array([x1, x2, x3])

H = sum((X - P) ** 2)
g = np.array([H.diff(x) for x in X])
G = np.array([[H.diff(x).diff(y) for x in X] for y in X])

X_num = np.array([0, 0, 0])
g_num = np.array([g_row.subs(zip(X, X_num)) for g_row in g])
G_num = G

# print(g)
# print(g_num)
# print(G)
# print(G_num)

F = H.subs(zip(X, X_num)) + g_num @ (X - X_num) + 0.5 * (G_num @ (X - X_num)) @ (X - X_num)

print(F)
