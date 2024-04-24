import numpy as np
import sympy as sp
from prettytable import PrettyTable
import matplotlib.pyplot as plt
plt.style.use('_mpl-gallery')

EPS = 0.0001

def f1(x, y):
    return 10 * pow((x + y - 10), 2) + pow((x - y + 4), 2)

def f2(x, y):
    return 100 * pow((y - pow(x, 2)), 2) + pow((1 - x), 2)

x01 = [0, 0]
x02 = [-1.2, 1]

def argmin(f, x0, S):
    delta = EPS/1000
    a, b = -1, 1

    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2

    while abs(b - a) > EPS/10:
        if f(x0[0] - x1 * S[0], x0[1] - x1 * S[1]) < f(x0[0] - x2 * S[0], x0[1] - x2 * S[1]):
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

def Broyden(f, X0: list[float]):
    table = PrettyTable()
    table = PrettyTable(["k", "x[0]", "x[1]", "f(x)", "|f(x(k)) - f(x(k-1))|"])
    xPlot = [X0[0]]
    yPlot = [X0[1]]
    """
    Метод Бройдена
    """
    # Начальные приготовления
    global EPS           # требуемая точность
    lastX = np.array(X0) # начальный вектор X
    lamb = 0
    Nu0 = np.eye(2)      # единичная матрица 2x2
    acc = 100            # текущая точность
    curGrad = np.array(gradient(f, lastX)) # текущий градиент
    i = 0
    S = Nu0 * (curGrad)        # считаем направление
    S = S.diagonal()
    
    # Цикл пока не достигнем нужной точности
    while acc > EPS:
        i += 1
        lastGrad = curGrad.copy() # обновляем градиент
        if i % 2 == 0:
            S = Nu0 * (lastGrad)        # считаем направление
            S = S.diagonal()
        lamb = argmin(f, lastX, S)
        curX = lastX - lamb * S

        table.add_row([i, curX[0], curX[1], f(curX[0], curX[1]), abs(f(lastX[0], lastX[1]) - f(curX[0], curX[1]))])
        xPlot.append(curX[0])
        yPlot.append(curX[1])
        
        curGrad = np.array(gradient(f, curX))
        deltGrad = curGrad - lastGrad
        deltX = curX - lastX
        delNu = ((deltX - Nu0 * deltGrad) * np.transpose(Nu0 * deltGrad)) / (np.transpose(deltGrad) * Nu0 * deltGrad)
        Nu0 += delNu
        acc = np.linalg.norm(curGrad)
        lastX = curX.copy()

    print(table)
    xPlot = np.array(xPlot)
    yPlot = np.array(yPlot)

    fig, ax = plt.subplots()
    ax.plot(xPlot, yPlot, linewidth=2.0)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()
    return curX

Broyden(f1, x01)
Broyden(f2, x02)




