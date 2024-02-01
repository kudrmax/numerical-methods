from collections import defaultdict
from prettytable import *


def calculateNum(n: int):
    return 32 / (n ** 2 + 9 * n + 20)


def calculateSum(N: int):
    s = 0
    for n in range(N):
        s += calculateNum(n)
    return s


def calculateData():
    N_list = [10 ** k for k in range(1, 6)]

    sums = {}
    errors = {}
    digits = defaultdict(int)
    exact_sum = 8

    for N in N_list:
        sums[N] = calculateSum(N)
        errors[N] = abs(sums[N] - exact_sum)

    for N in N_list:
        i = -1
        for i in range(0, 50):
            order_of_error = 1 / (10 ** i)
            if errors[N] <= order_of_error:
                digits[N] += 1
            else:
                break

    # for N in N_list:
    #     print(f"{sums[N]}\t±\t{errors[N]} \tс {digits[N]} значащих цифр, {N = }")

    table = PrettyTable()
    table.field_names = ["N", "Значение", "Погрешность", "Число значащих цифр"]
    table.align = 'l'
    for N in N_list:
        table.add_row([N, sums[N], errors[N], digits[N]])
    print(table)

    return {
        "sums": sums,
        "errors": errors,
        "digits": digits
    }
