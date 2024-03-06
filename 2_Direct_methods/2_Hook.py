import math
from prettytable import PrettyTable
global EPS

table = PrettyTable()
table.field_names = ["k", "x[0]", "x[1]", "f(x)", "|f(x(k)) - f(x(k-1))|", "delta"]

EPS = 0.000001

def f1(x, y):
    return 10 * pow((x + y - 10), 2) + pow((x - y + 4), 2)


def f2(x, y):
    return 100 * pow((y - pow(x, 2)), 2) + pow((1 - x), 2)


x01 = [0, 0]
x02 = [-1.2, 1]

def argmin(f, x, s):
    delta = EPS / 2
    count_iter = 0
    calc_count = 0
    a_i, b_i = 0, 20
    while abs(a_i - b_i) > EPS:
        x1 = (a_i + b_i - delta)/2
        x2 = (a_i + b_i + delta)/2
        if f(x[0] + x1 * s[0], x[1] + x1 * s[1]) > f(x[0] + x2 * s[0], x[1] + x2 * s[1]):
            a_i = x1
        else:
            b_i = x2
        count_iter += 1
        calc_count += 2
    return (a_i + b_i) / 2


def search(f, x, step):
    flag = 0
    f1 = 0
    f2 = 0
    x1 = x.copy()
    for i in range(2):
        x2 = x1.copy()
        x3 = x1.copy()
        oldF = f(x[0], x[1]) 
        x2[i] += step
        f1 = f(x2[0], x2[1])
        x3[i] -= step
        f2 = f(x3[0], x3[1])
        if f1 < f2 and (f1 < oldF or f2 < oldF):
            x1 = x2
            flag += 1
        else:
            x1 = x3
            flag += 1
    return x1



def hook_jeeves(f, x0, step):
    newX = x0.copy()
    newF = f(x0[0], x0[1])
    oldF = 0
    s = [0, 0]
    i = 1
    while abs(newF - oldF) > EPS:
        step = 0.1
        oldF = newF
        oldX = newX.copy()
        newX = search(f, oldX, step)
        newF = f(newX[0], newX[1])
        while(newF > oldF):
            newX = search(f, oldX, step)
            newF = f(newX[0], newX[1])
            step /= 2
        s[0] = float(newX[0] - oldX[0])
        s[1] = float(newX[1] - oldX[1])
        lam = argmin(f, oldX, s)
        newX[0] = oldX[0] + lam * s[0]
        newX[1] = oldX[1] + lam * s[1]
        newF = f(newX[0], newX[1])
        table.add_row([i, newX[0], newX[1], newF, math.fabs(newF - oldF), step])
        i += 1

hook_jeeves(f1, x01, 1)
print(table)
table.clear()
table.field_names = ["k", "x[0]", "x[1]", "f(x)", "|f(x(k)) - f(x(k-1))|", "delta"]
hook_jeeves(f2, x02, 1)
print(table)

    