import numpy as np
from scipy.stats import multivariate_normal
import time
## Task 1:

# Создаем файл с матрицей
matrix_content = """3,4,17,-3
5,11,-1,6
0,2,-5,8"""

with open('matrix.txt', 'w') as f:
    f.write(matrix_content)


matrix = []
with open('matrix.txt', 'r') as f:
    for line in f:
        row = [float(x) for x in line.strip().split(',')]
        matrix.append(row)

total_sum = sum(sum(row) for row in matrix)
min_val = min(min(row) for row in matrix)
max_val = max(max(row) for row in matrix)

print("Task 1 Results:")
print(f"Сумма элементов: {total_sum}")
print(f"Минимальный элемент: {min_val}")
print(f"Максимальный элемент: {max_val}\n")

# Task 2

def rle_encode(x):
    if len(x) == 0:
        return np.array([]), np.array([])
    
    values = []
    counts = []
    current = x[0]
    count = 1
    
    for val in x[1:]:
        if val == current:
            count += 1
        else:
            values.append(current)
            counts.append(count)
            current = val
            count = 1
            
    values.append(current)
    counts.append(count)
    
    return np.array(values), np.array(counts)

x = np.array([2, 2, 2, 3, 3, 3, 5])
values, counts = rle_encode(x)

print("Task 2 Results:")
print(f"Исходный вектор: {x}")
print(f"Значения: {values}")
print(f"Количество повторов: {counts}\n")

# Task 3


np.random.seed(0)  
data = np.random.normal(size=(10, 4))

stats = {
    "min": np.min(data),
    "max": np.max(data),
    "mean": np.mean(data),
    "std": np.std(data)
}
first_5 = data[:5]

print("Task 3 Results:")
print("Статистика:")
for key, value in stats.items():
    print(f"{key}: {value:.4f}")
print("\nПервые 5 строк:")
print(first_5)
print()

# Task 4:


x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
zero_mask = np.concatenate([[False], (x[:-1] == 0)])

if np.any(zero_mask):
    result = np.max(x[zero_mask])
else:
    result = None

print("Task 4 Results:")
print(f"Исходный вектор: {x}")
print(f"Максимальный элемент после нуля: {result}\n")

# Task 5:


def logpdf(X, m, C):
    D = X.shape[1]
    det = np.linalg.det(C)
    inv = np.linalg.inv(C)
    const = D * np.log(2 * np.pi) + np.log(det)
    
    diff = X - m
    exponent = -0.5 * np.sum(diff @ inv * diff, axis=1)
    return exponent - 0.5 * const


N, D = 1000, 3
X = np.random.randn(N, D)
m = np.zeros(D)
C = np.eye(D)


start_custom = time.time()
custom_log = logpdf(X, m, C)
custom_time = time.time() - start_custom


start_scipy = time.time()
scipy_log = multivariate_normal(m, C).logpdf(X)
scipy_time = time.time() - start_scipy


diff = np.max(np.abs(custom_log - scipy_log))

print("Task 5 Results:")
print(f"Наша реализация: {custom_time:.6f} сек")
print(f"Scipy: {scipy_time:.6f} сек")
print(f"Максимальная разница: {diff:.10f}\n")

# Task 6: 


a = np.arange(16).reshape(4, 4)
print("Task 6 Results:")
print("Исходная матрица:")
print(a)

a[[1, 3]] = a[[3, 1]]

print("\nПосле замены строк 1 и 3:")
print(a)
print()

# Task 7:

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:, -1]  # Последний столбец содержит виды
unique_species, counts = np.unique(species, return_counts=True)

print("Task 7 Results:")
for species, count in zip(unique_species, counts):
    print(f"{species.decode('utf-8')}: {count}")
print()
# Task 8: 

arr = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
nonzero_indices = np.nonzero(arr)[0]

print("Task 8 Results:")
print(f"Исходный вектор: {arr}")
print(f"Индексы ненулевых элементов: {nonzero_indices}")