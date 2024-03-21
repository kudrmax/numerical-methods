import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

# from optimize import root


def var_f(x: np.array) -> np.array:
    return np.array([np.sin(0.5 * x[0] + x[1]) - 1.2 * x[0] - 1,
                     x[0]**2 + x[1]**2 - 1], dtype=np.double)


# custom_solution_f, iter_cnt_f = root(var_f, np.array([-1, 0]))
# custom_solution_s, iter_cnt_s = root(var_f, np.array([1, 2]))
# scipy_solution_f = scipy.optimize.fsolve(var_f, np.array([-1, 0]))
# scipy_solution_s = scipy.optimize.fsolve(var_f, np.array([1, 2]))


# print(f'Newton\'s method first solution: {custom_solution_f}')
# print(f'Number of iterations: {iter_cnt_f}')
# print(f'Newton\'s method second solution: {custom_solution_s}')
# print(f'Number of iterations: {iter_cnt_s}')
# print(f'Scipy solutions: {scipy_solution_f}, {scipy_solution_s}')

# построить график

x1, x2 = np.meshgrid(np.arange(-2, 2, 0.05), np.arange(-2, 2, 0.05))
plt.figure(figsize=(6, 5))
plt.contour(x1, x2, np.cos(x1 + x2) + 2 * x2, [0], colors=['red'])
plt.contour(x1, x2, x1 + np.sin(x2) - 0.6, [0], colors=['orange'])
plt.savefig('image.png', dpi=300)
plt.show()