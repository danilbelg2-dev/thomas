import numpy as np

def f1(x, y):
    return (x**2 + 16) * y - 64

def f2(x, y):
    return (x - 2)**2 + (y - 2)**2 - 16

def F(x, y):
    return np.array([f1(x, y), f2(x, y)], dtype=float)

def J(x, y):
    # матрица Якоби (производные подсчитал на листочке)
    return np.array([
        [2 * x * y, x**2 + 16],
        [2 * (x - 2), 2 * (y - 2)]
    ], dtype=float)

# графически в десмосе определил начальное приближение x = 6, y = 1
# (занизил специально для проверки работы алгоритма). В десмосе хорошая точность что-то...

eps = 0.001
x = 6
y = 1
iter_count = 0

print("Метод Ньютона для системы:")
while True:
    F_val = F(x, y)
    J_val = J(x, y)
    
    # Решаем систему J * delta = -F
    delta = np.linalg.solve(J_val, -F_val)
    
    # Определяем новые значения
    x_old, y_old = x, y
    x = x + delta[0]
    y = y + delta[1]
    
    iter_count += 1
    diff = max(abs(x - x_old), abs(y - y_old))
    
    print(f"Итерация {iter_count}: x = {x:.5f}, y = {y:.5f}, погрешность = {diff:.2e}")
    
    if diff < eps:
        break

print(f"\n Ответ: x = {x:.5f}, y = {y:.5f}, итераций: {iter_count}")
print(f" Проверка f1 = {f1(x, y):.4f}, f2 = {f2(x, y):.4f}")

exit()
