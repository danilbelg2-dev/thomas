import numpy as np

# Матрица коэффициентов (симметричная)
a = np.array([
    [5,  5, 3],
    [5, -4, 1],
    [3,  1, 2]
], dtype=float)

n = 3
eps = 0.01
max_iter = 100 # На всякий

Q = np.eye(n) # Единичная матрица для матрицы поворота

print("\n Метод вращений:")
iter_count = 0

while iter_count < max_iter:
    max_off = 0.0
    p, q = 0, 1
    for i in range(n):
        for j in range(i + 1, n):
            if abs(a[i][j]) > max_off:
                max_off = abs(a[i][j])
                p, q = i, j
    
    if max_off < eps:
        break
    
    if a[p][p] == a[q][q]:
        theta = np.pi / 4
    else:
        theta = 0.5 * np.arctan(2 * a[p][q] / (a[p][p] - a[q][q]))
    
    c = np.cos(theta)
    s = np.sin(theta)
    
    R = np.eye(n)
    R[p][p] = c
    R[q][q] = c
    R[p][q] = -s
    R[q][p] = s
    
    a = R.T @ a @ R
    Q = Q @ R
    
    iter_count += 1
    print(f"Итерация {iter_count}: обнуляем a[{p+1}][{q+1}], угол = {theta:.4f}")

print(f"\n Всего итераций: {iter_count}")

print("\n Собственные значения (на диагонали):")
for i in range(n):
    print(f"λ[{i+1}] = {a[i][i]:.4f}")

print("\n Собственные векторы (столбцы матрицы Q):")
print(Q)

exit()