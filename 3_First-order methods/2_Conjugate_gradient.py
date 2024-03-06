import numpy as np
import sympy as sp
from prettytable import PrettyTable
import matplotlib.pyplot as plt
plt.style.use('_mpl-gallery')

global EPS
EPS = 0.001


table = PrettyTable()
table = PrettyTable(["k", "x[0]", "x[1]", "f(x)", "S[0]", "S[1]", "|f(x(k)) - f(x(k-1))|"])

def f1(x, y):
    return 10 * pow((x + y - 10), 2) + pow((x - y + 4), 2)

def f2(x, y):
    return 100 * pow((y - pow(x, 2)), 2) + pow((1 - x), 2)

x01 = [0, 0]
x02 = [-1.2, 1]


xPlot = []
yPlot = []

def argmin(f, x0, S):
    delta = EPS/1000
    a, b = -0.1, 0.1

    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2

    while abs(b - a) > EPS/10:
        if f(x0[0] + x1 * S[0], x0[1] + x1 * S[1]) < f(x0[0] + x2 * S[0], x0[1] + x2 * S[1]):
            b = x2
        else:
            a = x1
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
    # return [x0[0] + ((a + b) / 2) * S[0], x0[1] + ((a + b) / 2) * S[1]]
    return (x1 + x2)/2


def gradient(f, x0):
    u = sp.IndexedBase('u')
    grad = [0, 0]
    diff0 = sp.diff(f(u[0], u[1]), u[0])
    diff1 = sp.diff(f(u[0], u[1]), u[1])
    grad[0] = float(diff0.subs(u[0], x0[0]).subs(u[1], x0[1]))
    grad[1] = float(diff1.subs(u[0], x0[0]).subs(u[1], x0[1]))
    return grad
    

def conjugate_gradient(f, x0):
    x = x0.copy()
    grad = gradient(f, x)
    S = [-grad[j] for j in range(2)]
    # lamb = argmin(f, x, S)
    lamb = 0

    i = 0
    iters = 0

    while True:
        i += 1
        iters += 1
        if iters >= 2:
            S = [-grad[j] for j in range(2)]
            iters = 0

        x0 = x.copy()

        lamb = argmin(f, x, S)
        x = [x[j] + lamb * S[j] for j in range(2)]

        grad = gradient(f, x)
        grad0 = gradient(f, x0)
        w = (np.linalg.norm(grad)/np.linalg.norm(grad0))**2

        S = [-grad[j] + w*S[j] for j in range(2)]
        
        table.add_row([i, x[0], x[1], f(x[0], x[1]), S[0], S[1], abs(f(x0[0], x0[1]) - f(x[0], x[1]))])
        xPlot.append(x[0])
        yPlot.append(x[1])
        if np.linalg.norm(S) < EPS:
            break
    
    return x

    

# conjugate_gradient(f1, x01)
# print(table)
# # table.clear()
# # table.field_names = ["k", "x[0]", "x[1]", "f(x)", "S[0]", "S[1]", "|f(x(k)) - f(x(k-1))|"]
conjugate_gradient(f2, x02)
print(table)

xPlot = np.array(xPlot)
yPlot = np.array(yPlot)

fig, ax = plt.subplots()
ax.plot(xPlot, yPlot, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()