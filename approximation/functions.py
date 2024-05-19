import numpy as np

def get_x_list_extended(x_list, k=3):
    x_list_extended = []
    for i in range(len(x_list) - 1):
        d = x_list[i + 1] - x_list[i]
        delta = d / k
        for j in range(k):
            x_list_extended.append(x_list[i] + delta * j)
    x_list_extended.append(x_list[-1])
    x_list_extended = np.array(x_list_extended)
    return x_list_extended