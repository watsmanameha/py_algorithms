# Задание 5
#
# "В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве".

import random

arr = [random.randint(-5, 5) for i in range(10)]

print(arr)

neg_arr = []

for el in arr:
    if el < 0:
        neg_arr.append(el)

neg_arr.sort()

print(f'{neg_arr[-1]}, индекс = -1')
