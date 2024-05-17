import numpy as np
import matplotlib.pyplot as plt


def plot(x, y):
    plt.plot(x, y, 'ro')
    plt.show()


def mnk(x, y, m):
    m += 1

    b = np.empty(m)  # b
    g = np.empty((m, m))  # Г

    # заполняем b = (P^T)*P
    for j in range(m):
        b[j] = np.sum(y * x ** j)

    # заполняем Г = P*P
    for j in range(m):
        for k in range(m):
            g[j][k] = sum(x ** (k + j))

    best_coeffs = np.linalg.solve(g, b)

    def f(px):
        py = 0
        for i in range(m):
            py += best_coeffs[i] * px ** i
        return py

    return f


x = np.array([0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0])
y = np.array([1.019, 1.4889, 2.2079, 3.0548, 3.8648, 4.2161, 5.1180, 5.7661, 6.6720, 7.1960, 7.8551])
n = len(x)

# считаем сигмы для определения лучшего m
sigmas = []
for m in range(n):
    f = mnk(x, y, m)
    sigma = np.sqrt((1 / (n - m)) * np.sum((f(x) - y) ** 2))
    sigmas.append(sigma)

f = mnk(x, y, 1)

fig, axes = plt.subplots(ncols=2)
axes[0].scatter(x, y, c='r')
axes[0].plot(x, f(x))
axes[1].bar(x=np.arange(len(sigmas)), height=sigmas)
plt.show()
