import matplotlib.pyplot as plt

def solve_sys(A, b):
    # Решаем систему методом Гаусса
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    
    for k in range(n):
        if abs(M[k][k]) < 1e-12:
            for i in range(k + 1, n):
                if abs(M[i][k]) > 1e-12:
                    M[k], M[i] = M[i], M[k]
                    break

        for i in range(k + 1, n):
            factor = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= factor * M[k][j]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - s) / M[i][i]
    return x

def mnk(x, y, degree):
    # Формируем нормальную систему для МНК
    size = degree + 1
    A = [[0.0] * size for _ in range(size)]
    b = [0.0] * size

    for k in range(size):
        for i in range(size):
            A[k][i] = sum(val ** (k + i) for val in x)
        b[k] = sum(y[j] * x[j] ** k for j in range(len(x)))

    coef = solve_sys(A, b)
    return coef, A, b

def poly(coef, x):
    return sum(a * x**i for i, a in enumerate(coef))

def error(coef, x, y):
    # Сумма квадратов ошибок
    return sum((poly(coef, x[i]) - y[i])**2 for i in range(len(x)))

def print_poly(name, coef):
    text = f"{coef[0]:.5f}"
    for i in range(1, len(coef)):
        text += f" {coef[i]:+.5f}*x^{i}" if i > 1 else f" {coef[i]:+.5f}*x"
    print(f"{name}(x) = {text}")

# Данные 3-го варианта
x = [-0.9, 0.0, 0.9, 1.8, 2.7, 3.6]
y = [-0.36892, 0.0, 0.36892, 0.85408, 1.7856, 6.3138]

print("МНК, Вариант 3:")

# Строим 1-ю и 2-ю степени
coef1, A1, b1 = mnk(x, y, 1)
coef2, A2, b2 = mnk(x, y, 2)

print("\n Нормальная система для 1-й степени:")
for row, rhs in zip(A1, b1):
    print("  ".join(f"{v:10.4f}" for v in row), f"| {rhs:10.4f}")
print_poly("F1", coef1)
print(f" Сумма квадратов ошибок Ф1 = {error(coef1, x, y):.6f}")

print("\n Нормальная система для 2-й степени:")
for row, rhs in zip(A2, b2):
    print("  ".join(f"{v:10.4f}" for v in row), f"| {rhs:10.4f}")
print_poly("F2", coef2)
print(f" Сумма квадратов ошибок Ф2 = {error(coef2, x, y):.6f}")

# Построение графиков
x_plot = [min(x) + i * (max(x) - min(x)) / 100 for i in range(101)]

plt.figure()
plt.scatter(x, y, color='red', label="Исходные точки")
plt.plot(x_plot, [poly(coef1, z) for z in x_plot], label="F1(x)")
plt.plot(x_plot, [poly(coef2, z) for z in x_plot], label="F2(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод наименьших квадратов (Вариант 3)")
plt.grid()
plt.legend()
plt.show()

exit()