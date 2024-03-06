import numpy
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

from prettytable import PrettyTable
plt.style.use('_mpl-gallery')

global EPS

EPS = 0.0001

xPlot = []
yPlot = []

table = PrettyTable()
table = PrettyTable(["k", "x[0]", "x[1]", "f(x)", "S[0]", "S[1]", "|f(x(k)) - f(x(k-1))|"])

def f1(x, y):
    return 10 * pow((x + y - 10), 2) + pow((x - y + 4), 2)

def f2(x, y):
    return 100 * pow((y - pow(x, 2)), 2) + pow((1 - x), 2)

x01 = [0, 0]
x02 = [-1.2, 1]

def argmin(f, x0, S):
    delta = EPS / 10
    a, b = -0.1, 0.1

    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2

    while abs(b - a) > EPS:
        if f(x0[0] + x1 * S[0], x0[1] + x1 * S[1]) < f(x0[0] + x2 * S[0], x0[1] + x2 * S[1]):
            b = x2
        else:
            a = x1
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
    return (x1 + x2)/2


def gradient(f, x0):
    u = sp.IndexedBase('u')
    grad = [0, 0]
    diff0 = sp.diff(f(u[0], u[1]), u[0])
    diff1 = sp.diff(f(u[0], u[1]), u[1])
    grad[0] = float(diff0.subs(u[0], x0[0]).subs(u[1], x0[1]))
    grad[1] = float(diff1.subs(u[0], x0[0]).subs(u[1], x0[1]))
    return grad
    

def gradient_descent(f, x0):
    x = x0.copy()
    S = [0, 0]
    lamb = 0
    i = 0

    while True:
        i += 1
        x0 = x.copy()

        grad = gradient(f, x)
        norm = numpy.linalg.norm(grad)
        S = [-grad[j]/norm for j in range(2)]
        lamb = argmin(f, x, S)
        # lamb /= 2
        x = [x[j] + lamb * S[j] for j in range(2)]

        table.add_row([i, x[0], x[1], f(x[0], x[1]), S[0], S[1], abs(f(x0[0], x0[1]) - f(x[0], x[1]))])
        xPlot.append(x[0])
        yPlot.append(x[1])

        if abs(f(x0[0], x0[1]) - f(x[0], x[1])) and abs(x[0] - x0[0]) < EPS and abs(x[1] - x0[1]) < EPS:
            break
    
    return x

# gradient_descent(f1, x01)
# print(table)
# table.clear()
# table.field_names = ["k", "x[0]", "x[1]", "f(x)", "S[0]", "S[1]", "|f(x(k)) - f(x(k-1))|"]
gradient_descent(f2, x02)
print(table)

xPlot = np.array(xPlot)
yPlot = np.array(yPlot)

fig, ax = plt.subplots()
ax.plot(xPlot, yPlot, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

