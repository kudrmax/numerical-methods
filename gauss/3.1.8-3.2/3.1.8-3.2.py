import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

n = 6
N = 8
delta = 0.0005

with open('3.1.8-3.2.txt', "w") as f:
    # заполним матрицу A
    A = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            c = 0.1 * N * (i + 1) * (j + 1)
            A[i][j] = 1 / np.sqrt(c ** 2 + 0.58 * c)
    pd.DataFrame(A).to_csv('A.csv', float_format='%.5f')

    # заполним вектор b
    b = np.full(n, N, dtype=float)
    pd.DataFrame(b).to_csv('b.csv')

    # найдем лист из измененных векторов b
    b_error_list = []
    for i in range(n):
        b_error = b.copy()
        b_error[i] += delta
        b_error_list.append(b_error)

    # найдем лист из измененных матриц A
    A_error_list = []
    for i in range(n):
        A_error_row = []
        for j in range(n):
            A_error = A.copy()
            A_error[i][j] += delta
            A_error_row.append(A_error)
        A_error_list.append(A_error_row)

    # найдем решение через встроенную функцию
    x = np.linalg.solve(A, b)
    # print(f"{x = }", file=f)
    pd.DataFrame(x).to_csv('x.csv', float_format='%.6f')

    # найдем число обусловленности через встроенную функцию
    A_cond = np.linalg.cond(A, np.inf)
    print(f"{A_cond = }", file=f)

    # найдем вектор d для изменения b
    d_for_b = np.empty(n)
    for i in range(n):
        b_error = b_error_list[i]
        x_error = np.linalg.solve(A, b_error)
        d_for_b[i] = np.linalg.norm(x - x_error, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
    # print(f"{d_for_b = }", file=f)
    pd.DataFrame(d_for_b).to_csv('d_for_b.csv', float_format='%.6f')

    # найдем вектор d для изменения A
    d_for_A = np.empty(A.shape)
    for i in range(n):
        for j in range(n):
            A_error = A_error_list[i][j]
            x_error = np.linalg.solve(A_error, b)
            d_for_A[i][j] = np.linalg.norm(x - x_error, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
    # print(f"{d_for_A = }", file=f)
    pd.DataFrame(d_for_A).to_csv('d_for_A.csv', float_format='%.6f')

    # найдем что оказывает наибольшее влияние на погрешность для b
    d_for_b_max = d_for_b.max()
    d_for_b_max_index = list(d_for_b).index(d_for_b_max)
    print(f'Максимальный элемент d для b: {d_for_b_max} с индексом = {d_for_b_max_index}', file=f)


    # найдем что оказывает наибольшее влияние на погрешность для A
    d_for_A_max = d_for_A.max()
    # d_for_b_max_index = d_for_A.argmax()
    for i in range(n):
        for j in range(n):
            if d_for_A[i][j] == d_for_A_max:
                d_for_b_max_index = [i, j]
    print(f'Максимальный элемент d для A: {d_for_A_max} с индексом = {d_for_b_max_index}', file=f)

    # построим гистограмму для b
    plt.bar(range(n), d_for_b)
    plt.savefig('3.1.8.png', dpi=300)
    plt.show()

    # построим гистограмму для A
    data_2d = d_for_A
    data_array = np.array(data_2d)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    x_data, y_data = np.meshgrid(np.arange(data_array.shape[1]), np.arange(data_array.shape[0]))
    x_data = x_data.flatten()
    y_data = y_data.flatten()
    z_data = data_array.flatten()
    ax.bar3d(x_data, y_data, np.zeros(len(z_data)),
             0.5, 0.5, z_data)
    fig.tight_layout()
    plt.savefig('3.2.png', dpi=300)
    fig.show()

    # сделаем теоретическую оценку для b
    delta_rel_b = np.abs(delta) / np.linalg.norm(b, ord=np.inf)  # тоже что и np.linalg.norm(b - b_error, ord=np.inf) / np.linalg.norm(b, ord=np.inf)
    delta_rel_x_error_for_b = A_cond * delta_rel_b
    print(f'Теоретическая оценка для для b: {delta_rel_x_error_for_b}', file=f)

    # сделаем теоретическую оценку для A
    delta_rel_A = np.abs(delta) / np.linalg.norm(A, ord=np.inf)
    delta_rel_x_error_for_A = A_cond * delta_rel_A
    print(f'Теоретическая оценка для для A: {delta_rel_x_error_for_A}', file=f)

