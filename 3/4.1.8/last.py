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
X = np.array([x1, x2, x3])
Angle = np.array([phi, teta])


def from_angles_to_x(Angle):
    phi, teta = Angle
    x1 = a1 * sp.sin(phi) * sp.sin(teta)
    x2 = a2 * sp.cos(phi) * sp.sin(teta)
    x3 = a3 * sp.cos(phi)
    return np.array([x1, x2, x3])


P = P_list[0]

X_angles = from_angles_to_x(Angle)

H_angle = sum((X_angles - P) ** 2)

g_angle = sp.Matrix([H_angle.diff(angle) for angle in Angle])
G_angle = sp.Matrix([[H_angle.diff(angle1).diff(angle2) for angle1 in Angle] for angle2 in Angle])

print(f'{H_angle = }')
print(f'{g_angle = }')
print(f'{G_angle = }')

# H = sum((X - P) ** 2)
# print(H)

# g = np.array([H.diff(x) for x in X])
# G = np.array([[H.diff(x).diff(y) for x in X] for y in X])
# # F = H.subs(zip(X, X_num)) + g_num @ (X - X_num) + 0.5 * (G_num @ (X - X_num)) @ (X - X_num)
#
# print(f'{H = }')
# print(f'{g = }')
# print(f'{G = }')
#
X_angles_num = np.array([0, 0], dtype=float)

for _ in range(100):
    g_num = np.array(g_angle.subs(zip(Angle, X_angles_num)), dtype=float)
    G_num = np.array(G_angle.subs(zip(Angle, X_angles_num)), dtype=float)
    p_num = np.linalg.solve(G_num, -g_num).flatten()
    alpha = 1
    X_angles_num += alpha * p_num
    print(f'{X_angles_num = }')
