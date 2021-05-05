import numpy as np


def def_get_first_func(x):
    return np.sqrt((0.1 * (x ** 2) + x - 0.3) / -0.2)


def def_get_second_func(x):
    return (0.1 * (x ** 2) - 0.7) / (-1 + 0.1 * x)


def func1(x1, x2, k):
    return 0.1 * x1 ** 2 + x1 + 0.2 * x2 ** 2 - 0.3


def func2(x1, x2, k):
    return 0.2 * (x1 ** 2) + x2 - 0.1 * x1 * x2 - 0.7


def get_x1(x1, x2):
    return -0.1 * x1 ** 2 - 0.2 * x2 ** 2 + 0.3


def get_x2(x1, x2):
    return -0.2 * (x1 ** 2) + 0.1 * x1 * x2 + 0.7





def main(x1, x2, eps):
    x1_def = x1
    x2_def = x2
    new_x1 = 0
    new_x2 = 0
    k = 1

    while np.abs(x1_def - new_x1) > eps:

        if k > 1:
            x1_def = new_x1
            x2_def = new_x2

        new_x1 = get_x1(x1_def, x2_def)
        new_x2 = get_x2(x1_def, x2_def)
        print(k)
        print("x1_old : " + str(x1_def))
        print("x2_old : " + str(x2_def))
        print("div : " + str(np.abs(x1_def - new_x1)))
        print("x1 : " + str(new_x1))
        print("x2 : " + str(new_x2))
        print("--------------")
        k += 1
    print("Метод ітерацій")
    print("x1 : " + str(new_x1))
    print("x2 : " + str(new_x2))

x1 = 0.25
x2 = 0.75
eps = 0.0001
main(x1, x2, eps)
