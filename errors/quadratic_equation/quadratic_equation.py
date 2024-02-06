import numpy as np

eq = np.array([1, 27.4, 187.65])

c = 187.65
error = 0.005
errors = np.arange(-error, error, 2 * error / 20)

min_x1 = [-13.5125, -13.4875]
for error in errors:
    x = np.roots(eq + np.array([0, 0, error]))
    x1 = x[1]
    is_in_range = (min_x1[0] <= x1 <= min_x1[1])
    print(f"{x1 = },\t{error = },\t{is_in_range = }")

print()

min_x2 = [-13.9125, -13.8875]
for error in errors:
    x = np.roots(eq + np.array([0, 0, error]))
    x2 = x[0]
    is_in_range = (min_x2[0] <= x2 <= min_x2[1])
    print(f"{x2 = },\t{error = },\t{is_in_range = }")


