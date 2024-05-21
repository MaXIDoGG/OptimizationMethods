import numpy as np

def f1(x, y):
    return 10 * pow((x + y - 10), 2) + pow((x - y + 4), 2)

def f2(x, y):
    return 100 * pow((y - pow(x, 2)), 2) + pow((1 - x), 2)

def broyden_method(f, x0, y0, max_iter=100, tol=1e-6):
    x = np.array([x0, y0], dtype=float)
    Hk = np.eye(2)  # Initial approximation of the inverse Hessian matrix
    for _ in range(max_iter):
        gradient = np.array([
            -400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0]),
            200 * (x[1] - x[0]**2)
        ])
        pk = -np.dot(Hk, gradient)
        if np.linalg.norm(pk) < tol:
            break
        x_new = x + pk
        sk = x_new - x
        yk = gradient - np.array([
            -400 * x_new[0] * (x_new[1] - x_new[0]**2) - 2 * (1 - x_new[0]),
            200 * (x_new[1] - x_new[0]**2)
        ])
        yk = yk.reshape(-1, 1)
        Hk += np.dot((sk - np.dot(Hk, yk)) * sk.reshape(-1, 1), Hk) / np.dot(sk, yk)
        x = x_new
    return x

# Пример использования:
x_opt, y_opt = broyden_method(f1, 0, 0)
print("Минимум достигается в точке:", (x_opt, y_opt))
print("Значение функции в этой точке:", f2(x_opt, y_opt))
