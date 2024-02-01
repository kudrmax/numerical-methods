from calculate_sum import *
import matplotlib.pyplot as plt


def createPlots():
    data = calculateData()
    sums = data["sums"]
    errors = data["errors"]
    digits = data["digits"]

    keys_list = list(map(str, sums.keys()))
    errors_list = list(errors.values())
    digits_list = list(digits.values())

    bars = plt.barh(keys_list, errors_list, label='Погрешность')
    plt.bar_label(bars, padding=8, fontsize=9)
    plt.xlim(0, 14)
    plt.legend()
    plt.savefig('errors.png', dpi=300)
    plt.close()

    bars = plt.barh(keys_list, digits_list, label='Кол-во значимых цифр')
    plt.bar_label(bars, padding=8, fontsize=9)
    plt.xlim(0, 6)
    plt.legend()
    plt.savefig('digits.png', dpi=300)


createPlots()
