import matplotlib.pyplot as plt
import numpy as np

# region test
def def_get_first_func(x):
    return np.sqrt((0.1 * (x ** 2) + x - 0.3) / -0.2)


def def_get_second_func(x):
    return (0.1 * (x ** 2) - 0.7) / (-1 + 0.1 * x)


def func1(x1, x2, k):
    return 0.1 * x1 ** 2 + x1 + 0.2 * x2 ** 2 - 0.3


def func2(x1, x2, k):
    return 0.2 * (x1 ** 2) + x2 - 0.1 * x1 * x2 - 0.7


def f1_deriv_X1(x1, x2, k):
    return 0.2 * (x1) + 1


def f1_deriv_X2(x1, x2, k):
    return 0.4 * x2


def f2_deriv_X1(x1, x2, k):
    return 0.4 * x1 - 0.1 * x2


def f2_deriv_X2(x1, x2, k):
    return 1 - 0.1 * x1




def get_graph():
    fig = plt.subplots()
    x = np.linspace(-15, 5, 10000000)
    x1 = np.linspace(-10, 3, 100)
    plt.plot(x, def_get_first_func(x),  color="green")
    plt.plot(x, -def_get_first_func(x), color="green")
    plt.plot(x1, def_get_second_func(x1), color="blue")
    plt.grid()
    plt.show()


def J_mat(x1, x2, k):
    mat = [[], []]
    mat[0].append(f1_deriv_X1(x1, x2, k))
    mat[0].append(f1_deriv_X2(x1, x2, k))
    mat[1].append(f2_deriv_X1(x1, x2, k))
    mat[1].append(f2_deriv_X2(x1, x2, k))
    return determinant(mat)


def A1_mat(x1, x2, k):
    mat = [[], []]
    mat[0].append(func1(x1, x2, k))
    mat[0].append(f1_deriv_X2(x1, x2, k))
    mat[1].append(func2(x1, x2, k))
    mat[1].append(f2_deriv_X2(x1, x2, k))
    return determinant(mat)


def A2_mat(x1, x2, k):
    mat = [[], []]
    mat[0].append(f1_deriv_X1(x1, x2, k))
    mat[0].append(func1(x1, x2, k))
    mat[1].append(f2_deriv_X1(x1, x2, k))
    mat[1].append(func2(x1, x2, k))
    return determinant(mat)


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

        new_x1 = x1_def - (A1_mat(x1_def, x2_def, k) / J_mat(x1_def, x2_def, k))
        new_x2 = x2_def - (A2_mat(x1_def, x2_def, k) / J_mat(x1_def, x2_def, k))
        print(k)
        print("x1_old : " + str(x1_def))
        print("x2_old : " + str(x2_def))

        print("f1|x1 : " + str(f1_deriv_X1(x1, x2, k)))
        print("f2|x1 : " + str(f2_deriv_X1(x1, x2, k)))
        print("f1|x2 : " + str(f1_deriv_X2(x1, x2, k)))
        print("f2|x2 : " + str(f2_deriv_X2(x1, x2, k)))
        print("A1 : " + str(A1_mat(x1_def, x2_def, k)))
        print("A2 : " + str(A2_mat(x1_def, x2_def, k)))
        print("J : " + str(J_mat(x1_def, x2_def, k)))
        print("div : " + str(np.abs(x1_def - new_x1)))
        print("x1 : " + str(new_x1))
        print("x2 : " + str(new_x2))
        print("--------------")
        k += 1
    print(new_x1)
    print(new_x2)


def determinant(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


x01 = 0.25
x02 = 0.75
eps = 0.001
get_graph()
main(x01, x02, eps)
