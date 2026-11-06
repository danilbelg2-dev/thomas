def thomas_method(lower, main, upper, rhs):
    # Прямой и обратный ход метода прогонки
    n = len(rhs)
    p = [0.0] * n
    q = [0.0] * n

    p[0] = -upper[0] / main[0]
    q[0] = rhs[0] / main[0]

    for i in range(1, n):
        denominator = main[i] + lower[i] * p[i - 1]
        if i < n - 1:
            p[i] = -upper[i] / denominator
        q[i] = (rhs[i] - lower[i] * q[i - 1]) / denominator

    result = [0.0] * n
    result[-1] = q[-1]

    for i in range(n - 2, -1, -1):
        result[i] = p[i] * result[i + 1] + q[i]

    return result

def build_spline(x, f):
    n = len(x) - 1
    h = [x[i + 1] - x[i] for i in range(n)]

    c_nodes = [0.0] * (n + 1)

    m = n - 1
    lower = [0.0] * m
    main = [0.0] * m
    upper = [0.0] * m
    rhs = [0.0] * m

    for row in range(m):
        i = row + 1
        if row > 0:
            lower[row] = h[i - 1]
        main[row] = 2 * (h[i - 1] + h[i])
        if row < m - 1:
            upper[row] = h[i]

        rhs[row] = 3 * (
            (f[i + 1] - f[i]) / h[i]
            - (f[i] - f[i - 1]) / h[i - 1]
        )

    internal = thomas_method(lower, main, upper, rhs)

    for i in range(1, n):
        c_nodes[i] = internal[i - 1]

    a = [0.0] * n
    b = [0.0] * n
    c = [0.0] * n
    d = [0.0] * n

    for i in range(n):
        a[i] = f[i]
        c[i] = c_nodes[i]
        b[i] = (
            (f[i + 1] - f[i]) / h[i]
            - h[i] * (2*c_nodes[i] + c_nodes[i + 1]) / 3
        )
        d[i] = (c_nodes[i + 1] - c_nodes[i]) / (3*h[i])

    return a, b, c, d

def spline_value(x_nodes, coeffs, x_star):
    a, b, c, d = coeffs

    interval = 0
    for i in range(len(a)):
        if x_nodes[i] <= x_star <= x_nodes[i + 1]:
            interval = i
            break

    dx = x_star - x_nodes[interval]
    value = (
        a[interval]
        + b[interval]*dx
        + c[interval]*dx**2
        + d[interval]*dx**3
    )
    return value, interval

# Данные 3-го варианта
x = [0.0, 0.9, 1.8, 2.7, 3.6]
f = [0.0, 0.36892, 0.85408, 1.7856, 6.3138]
x_star = 1.5

print("Кубический сплайн (Вариант 3):")

coeffs = build_spline(x, f)
a, b, c, d = coeffs

print("\n Коэффициенты сплайна:")
print(" i       интервал          a_i          b_i          c_i          d_i")
for i in range(len(a)):
    print(
        f"{i+1:2d}    [{x[i]:.1f}, {x[i+1]:.1f}]    "
        f"{a[i]:11.5f}  {b[i]:11.5f}  {c[i]:11.5f}  {d[i]:11.5f}"
    )

value, interval = spline_value(x, coeffs, x_star)
print(f"\n X* = {x_star}")
print(f" Используется интервал [{x[interval]}, {x[interval+1]}]")
print(f" S(X*) = {value:.6f}")

exit()