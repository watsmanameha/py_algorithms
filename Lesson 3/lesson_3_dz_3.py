# Задание 3
#
# "В массиве случайных целых чисел поменять местами минимальный и максимальный элементы"

import random

arr = [random.randint(0, 10) for i in range(10)]

print(arr)

index_max = arr.index(max(arr))
index_min = arr.index(min(arr))

arr[index_max], arr[index_min] = arr[index_min], arr[index_max]

print(arr)
