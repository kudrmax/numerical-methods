from calculate_sum import *
import matplotlib.pyplot as plt


def createPlots():
    df = calculateData()

    df.plot.bar(x='N', y='Число значащих цифр')
    plt.title('Число значащих цифр')
    plt.xlabel('N')
    plt.ylabel('Число значащих цифр')
    plt.savefig('digits.png', bbox_inches='tight', dpi=300)
    plt.close()

    df.plot.bar(x='N', y='Погрешность')
    plt.title('Погрешность')
    plt.xlabel('N')
    plt.ylabel('Погрешность')
    plt.savefig('errors.png', bbox_inches='tight', dpi=300)
    plt.close()


createPlots()
