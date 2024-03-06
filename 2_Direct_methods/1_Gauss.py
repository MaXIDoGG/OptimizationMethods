import math
from prettytable import PrettyTable
global EPS

EPS = 0.0000001

table = PrettyTable()
table.field_names = ["k", "x[0]", "x[1]", "f(x)", "|f(x(k)) - f(x(k-1))|"]

def f1(x, y):
    return 10 * pow((x + y - 10), 2) + pow((x - y + 4), 2)


def f2(x, y):
    return 100 * pow((y - pow(x, 2)), 2) + pow((1 - x), 2)

x01 = [0, 0]
x02 = [-1.2, 1]


def argmin(f, x0, s):
    delta = EPS / 10
    a, b = -10, 10

    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2

    while abs(b - a) > EPS:
        if f(x0[0] + x1 * s[0], x0[1] + x1 * s[1]) < f(x0[0] + x2 * s[0], x0[1] + x2 * s[1]):
            b = x2
        else:
            a = x1
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
    return [x0[0] + ((a + b) / 2) * s[0], x0[1] + ((a + b) / 2) * s[1]]

def Gauss(f, x0):
    x = x0.copy()
    i = 0
    while True:
        x0[0], x0[1] = x[0], x[1]
        x = argmin(f, x, [1, 0])
        x = argmin(f, x, [0, 1])
        i += 1

        table.add_row([i, x[0], x[1], f(x[0], x[1]), abs(f(x0[0], x0[1]) - f(x[0], x[1]))])

        if abs(f(x0[0], x0[1]) - f(x[0], x[1])) < EPS:
            break

    return x

res = Gauss(f1, x01)
print(table)
table.clear()
table.field_names = ["k", "x[0]", "x[1]", "f(x)", "|f(x(k)) - f(x(k-1))|"]
res = Gauss(f2, x02)
print(table)