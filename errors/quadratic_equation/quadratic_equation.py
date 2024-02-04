import numpy as np

eq = np.array([1, 27.4, 187.65])

for error in [1 / (10**k) for k in range(1, 21)]:
    x = np.roots(eq + np.array([0, 0, error]))
    x1 = x[0]
    x2 = x[1]
    print(f"{x1 = },\t{x2 = },\t{error = }")
