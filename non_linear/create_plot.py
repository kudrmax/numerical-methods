import numpy as np
import matplotlib.pyplot as plt

x1, x2 = np.meshgrid(np.arange(-10, 10, 0.05), np.arange(-10, 10, 0.05))
plt.figure(figsize=(6, 5))
plt.contour(x1, x2, np.cos(x1 + x2) + 2 * x2, [0], colors=['red'])
plt.contour(x1, x2, x1 + np.sin(x2) - 0.6, [0], colors=['blue'])
plt.savefig('nonlinear_newton.png', dpi=300)
plt.show()