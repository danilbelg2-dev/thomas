import numpy as np
import math
import matplotlib.pyplot as plt

# Задание 3.4. Вычисление производных табличной функции (Вариант 3)
x_nodes = np.array([1.0, 1.5, 2.0, 2.5, 3.0], dtype=float)
y_nodes = np.array([0.0, 0.40547, 0.69315, 0.91629, 1.0986], dtype=float)

x_star_deriv = 2.0
idx = 2 # Индекс точки x=2.0
h = 0.5 # Шаг

# Первая производная (центральная разность)
dy1 = (y_nodes[idx+1] - y_nodes[idx-1]) / (2 * h)
# Вторая производная (центральная разность)
dy2 = (y_nodes[idx+1] - 2 * y_nodes[idx] + y_nodes[idx-1]) / (h**2)

print(f"Первая производная в x = {x_star_deriv}: dy/dx = {dy1:.5f}")
print(f"Вторая производная в x = {x_star_deriv}: d2y/dx2 = {dy2:.5f}\n")


# Задание 3.5. Вычисление интеграла (Вариант 3)
def f(x):
    return x / ((3 * x + 4)**3)

x0 = -1.0
x1 = 1.0
h1 = 0.5
h2 = 0.25

# Метод средних прямоугольников
def method_rectangles(f, a, b, h):
    n = int((b - a) / h)
    integral = 0
    for i in range(n):
        mid = a + i * h + h / 2
        integral += f(mid)
    return integral * h

# Метод трапеций
def method_trapezoids(f, a, b, h):
    n = int((b - a) / h)
    integral = f(a) + f(b)
    for i in range(1, n):
        integral += 2 * f(a + i * h)
    return (h / 2) * integral

# Метод Симпсона
def method_simpson(f, a, b, h):
    n = int((b - a) / h)
    if n % 2 != 0:
        raise ValueError("Число шагов для Симпсона должно быть четным")
    integral = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i % 2 != 0 else 2
        integral += coef * f(a + i * h)
    return (h / 3) * integral

print(f"С шагом h1 = {h1}:")
print(f"  Метод прямоугольников: {method_rectangles(f, x0, x1, h1):.5f}")
print(f"  Метод трапеций:        {method_trapezoids(f, x0, x1, h1):.5f}")
print(f"  Метод Симпсона:        {method_simpson(f, x0, x1, h1):.5f}")

print(f"С шагом h2 = {h2}:")
print(f"  Метод прямоугольников: {method_rectangles(f, x0, x1, h2):.5f}")
print(f"  Метод трапеций:        {method_trapezoids(f, x0, x1, h2):.5f}")
print(f"  Метод Симпсона:        {method_simpson(f, x0, x1, h2):.5f}")

# Уточнение по Рунге-Ромбергу на основе метода трапеций
I_h1 = method_trapezoids(f, x0, x1, h1)
I_h2 = method_trapezoids(f, x0, x1, h2)
I_rr = I_h2 + (I_h2 - I_h1) / 3

print(f"\n Уточнение по Рунге-Ромбергу: {I_rr:.6f}")

# А ТЕПЕРЬ ГРАФИКИИИИИИИИИИИИИИИИИИИИИИИ

# Визуализация геометрического смысла методов
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle(f'Геометрический смысл методов (Шаг h = {h2}, n = 8)', fontsize=14)

n_vis = int((x1 - x0) / h2)
x_vis = np.linspace(x0, x1, n_vis + 1)
y_vis = f(x_vis)

# 1. Метод прямоугольников
ax = axes[0]
x_plot = np.linspace(x0, x1, 200)
ax.plot(x_plot, f(x_plot), 'k-', linewidth=1.5)
for i in range(n_vis):
    x_left = x0 + i * h2
    x_right = x_left + h2
    mid = x_left + h2 / 2
    ax.fill_between([x_left, x_right], 0, f(mid), color='skyblue', alpha=0.5, edgecolor='blue')
ax.set_title('Метод прямоугольников')
ax.grid(True)

# 2. Метод трапеций
ax = axes[1]
ax.plot(x_plot, f(x_plot), 'k-', linewidth=1.5)
for i in range(n_vis):
    x_left = x0 + i * h2
    x_right = x_left + h2
    ax.fill_between([x_left, x_right], [f(x_left), f(x_right)], color='lightgreen', alpha=0.5, edgecolor='green')
ax.set_title('Метод трапеций')
ax.grid(True)

# 3. Метод Симпсона
ax = axes[2]
ax.plot(x_plot, f(x_plot), 'k-', linewidth=1.5)
for i in range(0, n_vis, 2):
    x_pts = np.linspace(x0 + i * h2, x0 + (i + 2) * h2, 20)
    ax.fill_between(x_pts, 0, f(x_pts), color='lightcoral', alpha=0.5, edgecolor='red')
ax.set_title('Метод Симпсона')
ax.grid(True)
plt.tight_layout()


# График зависимости погрешности от шага
# Вычисляем "истинное" значение с помощью метода Симпсона с очень мелким шагом
h_true = 0.001
F_true = method_simpson(f, x0, x1, h_true) 

h_values = np.linspace(0.5, 0.05, 20)
err_rect, err_trap, err_simp = [], [], []

for h_val in h_values:
    n_steps = int((x1 - x0) / h_val)
    # Корректировка шага для Симпсона (четное число шагов)
    if n_steps % 2 != 0:
        n_steps += 1
        h_val_actual = (x1 - x0) / n_steps
    else:
        h_val_actual = h_val

    val_rect = method_rectangles(f, x0, x1, h_val_actual)
    val_trap = method_trapezoids(f, x0, x1, h_val_actual)
    val_simp = method_simpson(f, x0, x1, h_val_actual)
    
    err_rect.append(abs(F_true - val_rect))
    err_trap.append(abs(F_true - val_trap))
    err_simp.append(abs(F_true - val_simp))

plt.figure(figsize=(10, 5))
plt.plot(h_values, err_rect, 'bs-', label='Прямоугольники')
plt.plot(h_values, err_trap, 'g^-', label='Трапеции')
plt.plot(h_values, err_simp, 'ro-', label='Симпсон')
plt.yscale('log')
plt.gca().invert_xaxis() # Шаг уменьшается слева направо
plt.title('Зависимость абсолютной погрешности от шага h')
plt.xlabel('Шаг h')
plt.ylabel('Абсолютная погрешность')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()

plt.show()

exit()