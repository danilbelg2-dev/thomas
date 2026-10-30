import math

def f(x):
    return math.tan(x)

# Интерполяция Лагранжа
print("Построение многочлена Лагранжа (столбец а)")
x_lag = [0, math.pi/8, 2*math.pi/8, 3*math.pi/8]
y_lag = [f(x) for x in x_lag]

# Вывод базисных многочленов
for i in range(len(x_lag)):
    s = f"L_{i}(x) = {y_lag[i]:.4f}"
    for j in range(len(x_lag)):
        if i != j:
            s += f" * (x - {x_lag[j]:.4f}) / ({x_lag[i]:.4f} - {x_lag[j]:.4f})"
    print(s)

print("Многочлен Лагранжа: P(x) = Сумма( y_i * L_i(x) )")

# Интерполяция Ньютона
print("\n Построение многочлена Ньютона (столбец б)")
x_newt = [0, math.pi/8, math.pi/3, 3*math.pi/8]
y_newt = [f(x) for x in x_newt]

def divided_differences(x_nodes, y_nodes):
    n = len(x_nodes)
    coef = [[0.0] * n for _ in range(n)]
    for i in range(n):
        coef[i][0] = y_nodes[i]
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x_nodes[i+j] - x_nodes[i])
    return [coef[0][i] for i in range(n)]

coef_newt = divided_differences(x_newt, y_newt)

print("Коэффициенты (разделённые разности):")
for i, c in enumerate(coef_newt):
    print(f"a_{i} = {c:.7f}")

print("Многочлен Ньютона в общем виде:")
poly_str = f"P(x) = {coef_newt[0]:.4f}"
for i in range(1, len(coef_newt)):
    term = f" + {coef_newt[i]:.4f}"
    for j in range(i):
        term += f"*(x - {x_newt[j]:.4f})"
    poly_str += term
print(poly_str)

# Вычисление в точке X*
x_star = 3 * math.pi / 16

def lagrange(x_val, x_nodes, y_nodes):
    result = 0.0
    for i in range(len(x_nodes)):
        term = y_nodes[i]
        for j in range(len(x_nodes)):
            if i != j:
                term *= (x_val - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

def newton(x_val, x_nodes, coef):
    result = coef[0]
    for i in range(1, len(coef)):
        term = coef[i]
        for j in range(i):
            term *= (x_val - x_nodes[j])
        result += term
    return result

y_lagrange = lagrange(x_star, x_lag, y_lag)
y_newton = newton(x_star, x_newt, coef_newt)

print(f"\n--- Результаты в точке X* = {x_star:.5f} ---")
print(f"Точное значение f(X*) = {f(x_star):.7f}")
print(f"Лагранж: P(X*) = {y_lagrange:.7f}, погрешность = {abs(f(x_star) - y_lagrange):.2e}")
print(f"Ньютон:  P(X*) = {y_newton:.7f}, погрешность = {abs(f(x_star) - y_newton):.2e}")

exit()