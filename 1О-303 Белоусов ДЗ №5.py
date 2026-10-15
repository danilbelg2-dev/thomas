import math

def f(x):
    return math.sqrt(1-x**2) - math.exp(x) + 0.1
def g(x):
    return math.log(math.sqrt(1 - x**2) + 0.1)

# т.к. 1-x**2 >= 0, x принадлежит отрезку [-1, 1], т.к. нужен положительный корень, то x принадлежит отрезку [0, 1]
# графически было определено начальное приближение x = 0.09

def df(x):
    # производная для метода Ньютона
    return -x / math.sqrt(1 - x**2) - math.exp(x)

eps = 0.001
x = 0.09
iter_count = 0

print("Метод простой итерации:")
while True:
    x_old = x
    x = g(x)
    iter_count += 1
    diff = abs(x - x_old)
    print(f"Итерация {iter_count}: x = {x:.7f}, погрешность = {diff:.2e}")
    if diff < eps:
        break

print(f"\n Ответ: x = {x:.5f}, итераций: {iter_count}")
print(f" Проверка f(x) = {f(x):.4f}")


# Метод Ньютона
print("\n Метод Ньютона:")
x = 0.09
iter_count = 0
while True:
    x_old = x
    x = x - f(x) / df(x)
    iter_count += 1
    diff = abs(x - x_old)
    print(f"Итерация {iter_count}: x = {x:.7f}, погрешность = {diff:.2e}")
    if diff < eps:
        break

print(f"\n Ответ: x = {x:.5f}, итераций: {iter_count}")
print(f" Проверка f(x) = {f(x):.4f}")

exit()