# Задание 9
#
# "Найти максимальный элемент среди минимальных элементов столбцов матрицы"


import random

N = 4
matrix = [[random.randint(0, 20) for _ in range(N)] for _ in range(N + 1)]
min_in_str = []

print(matrix)

for el in matrix:
    for i in el:
        min_in_str.append(min(el))

print(max(min_in_str))




