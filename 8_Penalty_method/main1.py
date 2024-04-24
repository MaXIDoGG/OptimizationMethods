from scipy.optimize import minimize

# rz = lambda x: (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2
rz = lambda x: 10 * pow((x[0] + x[1] - 10), 2) + pow((x[0] - x[1] + 4), 2)
h_1 = lambda x: (x[0] - 2 * x[1] + 2)
h_2 = lambda x: (-x[0] - 2 * x[1] + 6)
h_3 = lambda x: (-x[0] + 2 * x[1] + 2)

curr_func = lambda x: rz(x) + r * (1.0 / (h_1(x) ** 2 + h_2(x) ** 2 + h_3(x) ** 2))


x_c = [0, 0]
i = 1
r = 1
b = 0.2
eps = 0.001
while i < 1000:
    if curr_func(x_c) < eps:
        break
    curr_func = lambda x: rz(x) + r * (1.0 / (h_1(x) ** 2 + h_2(x) ** 2 + h_3(x) ** 2))
    x_c = minimize(curr_func, x_c).x
    i += 1
    r *= b
print(x_c)
print(i)
