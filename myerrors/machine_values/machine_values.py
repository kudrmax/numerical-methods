import numpy as np


def print_zero(my_type):
    k = 0
    num = my_type(1)
    while num != 0:
        num = my_type(num / 2)
        k += 1
    print(my_type, f"машинный ноль = 2^-{k}")


def print_infinity(my_type):
    k = 0
    num = my_type(1)
    while num != np.inf:
        num = my_type(num * 2)
        k += 1
    print(my_type, f"машинная бесконечность = 2^{k}")


def print_epsilon(my_type):
    k = 0
    num = my_type(1)
    while my_type(1.) + num > my_type(1.):
        num = my_type(num / 2)
        k += 1
    print(my_type, f"машинное эпсилон = 2^-{k}")


for my_type in [np.single, np.double, np.longdouble]:
    print_zero(my_type)
    print_infinity(my_type)
    print_epsilon(my_type)
    print()
