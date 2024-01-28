import pandas as pd


def calculateNum(n: int):
    return 32 / (n ** 2 + 9 * n + 20)


def calculateSum(N: int):
    s = 0
    for n in range(N):
        s += calculateNum(n)
    return s


def calculateData():
    N_list = [int(10 ** k) for k in range(1, 6)]

    sums = {}
    errors = {}
    digits = {}
    exact_sum = 8

    for N in N_list:
        sums[N] = calculateSum(N)
        errors[N] = abs(sums[N] - exact_sum)

    for N in N_list:
        digits[N] = 0
        for i in range(0, 50):
            order_of_error = 1 / (10 ** i)
            if errors[N] <= order_of_error:
                digits[N] += 1
            else:
                break

    sums_list = []
    errors_list = []
    digits_list = []
    for N in N_list:
        sums_list.append(sums[N])
        errors_list.append(errors[N])
        digits_list.append(digits[N])

    pd.options.display.float_format = '{:,.8f}'.format
    df = pd.DataFrame({
        'N': N_list,
        "Значение": sums_list,
        "Погрешность": errors_list,
        "Число значащих цифр": digits_list
    })
    return df


df = calculateData()
print(df)
df.to_latex("table.tex")
