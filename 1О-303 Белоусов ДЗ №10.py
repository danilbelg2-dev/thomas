import math

def f(x, y):
    return -y**2 - 1.0 / (x**4)

def exact(x):
    return (x - math.tan((x - 1.0) / x)) / (x**2)
# в задании походу ошибка, в формуле пминус лишний

x0 = 1.0
x_end = 2.0
y0 = 1.0
h = 0.1
n = int((x_end - x0) / h)

x_vals = [x0 + i * h for i in range(n + 1)]
y_euler = [0.0] * (n + 1)
y_euler_imp = [0.0] * (n + 1)
y_rk4 = [0.0] * (n + 1)
y_exact = [0.0] * (n + 1)

y_euler[0] = y0
y_euler_imp[0] = y0
y_rk4[0] = y0
y_exact[0] = exact(x0)

# Метод Эйлера
for i in range(n):
    y_euler[i + 1] = y_euler[i] + h * f(x_vals[i], y_euler[i])

# Улучшенный метод Эйлера
for i in range(n):
    k1 = f(x_vals[i], y_euler_imp[i])
    k2 = f(x_vals[i] + h, y_euler_imp[i] + h * k1)
    y_euler_imp[i + 1] = y_euler_imp[i] + (h / 2.0) * (k1 + k2)

# Метод Рунге-Кутты 4-го порядка
for i in range(n):
    k1 = f(x_vals[i], y_rk4[i])
    k2 = f(x_vals[i] + h / 2.0, y_rk4[i] + (h / 2.0) * k1)
    k3 = f(x_vals[i] + h / 2.0, y_rk4[i] + (h / 2.0) * k2)
    k4 = f(x_vals[i] + h, y_rk4[i] + h * k3)
    y_rk4[i + 1] = y_rk4[i] + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

# Точное решение
for i in range(n + 1):
    y_exact[i] = exact(x_vals[i])

print(f"{'x':<5} | {'Эйлер':<10} | {'Улучш. Эйлер':<12} | {'РК4':<10} | {'Точное':<10}")
print("-" * 55)
for i in range(n + 1):
    print(f"{x_vals[i]:<5.1f} | {y_euler[i]:<10.6f} | {y_euler_imp[i]:<12.6f} | {y_rk4[i]:<10.6f} | {y_exact[i]:<10.6f}")