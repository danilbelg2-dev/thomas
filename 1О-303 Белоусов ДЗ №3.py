import numpy as np

# Матрица коэффициентов и вектор правой части
a = np.array([
    [-23, -7,  5,  2],
    [ -7, -21, 4,  9],
    [  9,  5, -31, -8],
    [  0,  1,  -2, 10]
], dtype=float)

b = np.array([-26, -55, -58, -24], dtype=float)

n = 4
eps = 0.01

# Метод простых итераций
print("\n Метод простых итераций:")
x = np.zeros(n)  # начальное приближение
x_old = np.zeros(n)
iter_count = 0

while True:
    x_old = x.copy()
    for i in range(n):
        s = sum(a[i][j] * x_old[j] for j in range(n) if j != i)
        x[i] = (b[i] - s) / a[i][i]
    
    iter_count += 1
    # Проверка условия выхода из цикла
    diff = max(abs(x[i] - x_old[i]) for i in range(n))
    print(f"Итерация {iter_count}: x = {x}, погрешность = {diff:.3f}")
    
    if diff < eps:
        break

print("\n Ответ:")
for i in range(n):
    print(f"x[{i+1}] = {x[i]:.4f}")

# Метод Зейделя
print("\n Метод Зейделя:")
x = np.zeros(n) 
iter_count = 0

while True:
    x_old = x.copy()
    for i in range(n):
        s1 = sum(a[i][j] * x[j] for j in range(i))       # уже обновлённые
        s2 = sum(a[i][j] * x_old[j] for j in range(i+1, n))  # старые
        x[i] = (b[i] - s1 - s2) / a[i][i]
    
    iter_count += 1
    diff = max(abs(x[i] - x_old[i]) for i in range(n))
    print(f"Итерация {iter_count}: x = {x}, погрешность = {diff:.3f}")
    
    if diff < eps:
        break

print(f"\n Ответ:")
for i in range(n):
    print(f"x[{i+1}] = {x[i]:.4f}")

exit()