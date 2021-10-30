# Задание 2
#
# "Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа".

import random
arr1 = [random.randint(0, 10) for i in range(10)]
print(arr1)

arr2 = [el for el in arr1 if el % 2 == 0]

print(f'Четные элементы в массиве arr1:\n{arr2}')

arr2 = []

i = 0                   # Создадим счётчик
for el in arr1:
    if el % 2 == 0:
        arr2.append(i)
    i += 1

print(f'Индексы чётных элементов в массиве arr1:\n{arr2}')