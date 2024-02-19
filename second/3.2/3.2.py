import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

output_file_path = "3.2.txt"

n = 6
N = 8
delta = 0.05

os.remove(output_file_path)
with open(output_file_path, "a") as f:
    # заполним матрицу A
    A = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            c = 0.1 * N * (i + 1) * (j + 1)
            A[i][j] = 1 / np.sqrt(c ** 2 + 0.58 * c)

    # заполним вектор b
    b = np.full(n, N, dtype=float)

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
    print(f"{x = }", file=f)

    # найдем число обусловленности через встроенную функцию
    A_cond = np.linalg.cond(A, np.inf)
    print(f"{A_cond = }", file=f)

    # найдем вектор d для изменения b
    d_for_b = np.empty(n)
    for i in range(n):
        b_error = b_error_list[i]
        x_error = np.linalg.solve(A, b_error)
        d_for_b[i] = np.linalg.norm(x - x_error, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
    print(f"{d_for_b = }", file=f)

    # найдем вектор d для изменения A
    d_for_A = np.empty(A.shape)
    for i in range(n):
        for j in range(n):
            A_error = A_error_list[i][j]
            x_error = np.linalg.solve(A_error, b)
            d_for_A[i][j] = np.linalg.norm(x - x_error, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
    print(f"{d_for_A = }", file=f)

    # найдем что оказывает наибольшее влияние на погрешность для b
    d_for_b_max = d_for_b.max()
    d_for_b_max_index = list(d_for_b).index(d_for_b_max)
    print(f'{d_for_b_max = } with index = {d_for_b_max_index}', file=f)

    # найдем что оказывает наибольшее влияние на погрешность для A
    d_for_A_max = d_for_A.max()
    # d_for_b_max_index = d_for_A.argmax()
    for i in range(n):
        for j in range(n):
            if d_for_A[i][j] == d_for_A_max:
                d_for_b_max_index = [i, j]
    print(f'{d_for_A_max = } with index = {d_for_b_max_index}', file=f)

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

    # сравним погрешности для b
    # print(f"Сравнение погрешностей для b:", file=f)
    delta_rel_x_error_list = np.empty(n, dtype=float)
    for i in range(n):
        b_error = b_error_list[i]
        # delta_rel_b_old = np.linalg.norm(b - b_error, ord=np.inf) / np.linalg.norm(b, ord=np.inf)
        delta_rel_b = np.abs(delta) / np.linalg.norm(b, ord=np.inf)
        delta_rel_x_error = A_cond * delta_rel_b
        delta_rel_x_error_list[i] = delta_rel_x_error
        # print(f"практически: {d_for_b[i]},\tтеоритически: {delta_rel_x_error}", file=f)

    df_for_b = pd.DataFrame({
        'Индекс': list(range(n)),
        'Практические': d_for_b,
        "Теоретические": delta_rel_x_error_list
    })
    df_for_b.to_latex("3.1.8.tex", index=False)

    # сравним погрешности для b
    # print(f"Сравнение погрешностей для A:", file=f)
    delta_rel_x_error_list = np.empty(A.shape, dtype=float)
    for i in range(n):
        for j in range(n):
            A_error = A_error_list[i][j]
            delta_rel_A = np.abs(delta) / np.linalg.norm(A, ord=np.inf)
            delta_rel_x_error = A_cond * delta_rel_A
            delta_rel_x_error_list[i][j] = delta_rel_x_error
            # print(f"[{i}][{j}] практически: {d_for_A[i][j]},\tтеоритически: {delta_rel_x_error}", file=f)

    ids = np.empty((n, n), dtype=tuple)
    for i in range(n):
        for j in range(n):
            ids[i][j] = (i, j)
    df_for_A = pd.DataFrame({
        'i': ids.reshape(-1),
        'Практические': d_for_A.reshape(-1),
        "Теоретические": delta_rel_x_error_list.reshape(-1)
    })
    df_for_A.to_latex("3.2.tex", index=False)

with open(output_file_path, "r") as f:
    print(f.read())
