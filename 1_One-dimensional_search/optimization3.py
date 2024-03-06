import math
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["k", "a", "f(a)", "x1", "f(x1)", "x2", "f(x2)", "b", "f(b)", "|b - a|"]

def f(x):
    return 0.5 - (x/2)*math.exp(-pow(x/2, 2))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


A = 0
B = 5

e = 0.001
delt = 0.0001

x1 = None
x2 = None
n = 19

for i in range(1, n+1):
    if (x1 == None):
        x1 = (A + (fib(n-i+1)/fib(n-i+3)* (B - A)))
    if (x2 == None):
        x2 = (A + (fib(n-i+2)/fib(n-i+3)* (B - A)))

    dif = math.fabs(B-A)
    table.add_row([i, A, f(A), x1, f(x1), x2, f(x2), B, f(B), dif])

    if f(x1) < f(x2):
        B = x2
        x2 = x1
        x1 = None
    else:
        A = x1
        x1 = x2
        x2 = None
    

print(table)