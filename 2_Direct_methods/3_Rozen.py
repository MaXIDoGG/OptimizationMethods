import numpy as np
from prettytable import PrettyTable
global EPS

table = PrettyTable(["k", "x[0]", "x[1]", "f(x)", "|f(x(k)) - f(x(k-1))|"])

def f1(x, y):
    return 10 * pow((x + y - 10), 2) + pow((x - y + 4), 2)


def f2(x, y):
    return 100 * pow((y - pow(x, 2)), 2) + pow((1 - x), 2)


x01 = [0, 0]
x02 = [-1.2, 1]
EPS = 0.0001

def argmin(f, x0, s):
    delta = EPS / 10
    a, b = -0.1, 0.1

    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2

    while abs(b - a) > EPS:
        if f(x0[0] + x1 * s[0], x0[1] + x1 * s[1]) < f(x0[0] + x2 * s[0], x0[1] + x2 * s[1]):
            b = x2
        else:
            a = x1
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
    return (a + b) / 2


def Palmer(lamb, s0):
    A = [[lamb[0] * s0[0][0] + lamb[1] * s0[1][0], lamb[0] * s0[0][1] + lamb[1] * s0[1][1]],
         [lamb[1] * s0[1][0], lamb[1] * s0[1][1]]]
    Norm_a = [pow(A[0][0] * A[0][0] + A[0][1] * A[0][1], 0.5),
              pow(A[1][0] * A[1][0] + A[1][1] * A[1][1], 0.5)]
    Big_norm = Norm_a[1] * Norm_a[0] * pow(pow(Norm_a[0], 2) - pow(Norm_a[1], 2), 0.5)
    s = [[A[0][0] / Norm_a[0], A[0][1] / Norm_a[0]],
         [(A[1][0] * pow(Norm_a[0], 2) - A[0][0] * pow(Norm_a[1], 2)) / Big_norm,
          (A[1][1] * pow(Norm_a[0], 2) - A[0][1] * pow(Norm_a[1], 2)) / Big_norm]]
    return s


def Rosenbrock(f, x0):
    x = [x0[0], x0[1]]
    s = [[-1, 0], [0, -1]]
    i = 0
    while True:
        x0[0], x0[1] = x[0], x[1]
        lamb = [0, 0]
        lamb[0] = argmin(f, x, s[0])
        x[0] += lamb[0] * s[0][0]
        x[1] += lamb[0] * s[0][1]
        lamb[1] = argmin(f, x, s[1])
        x[0] += lamb[1] * s[1][0]
        x[1] += lamb[1] * s[1][1]
        s = Palmer(lamb, s)
        i += 1
        table.add_row([i, x[0], x[1], f(x[0], x[1]), abs(f(x0[0], x0[1]) - f(x[0], x[1]))])
        if abs(f(x0[0], x0[1]) - f(x[0], x[1])) < EPS:
            break
    return x


x = Rosenbrock(f1, x01)
print(table)
table.clear()
table.field_names = ["k", "x[0]", "x[1]", "f(x)", "|f(x(k)) - f(x(k-1))|"]
x = Rosenbrock(f2, x02)
print(table)
