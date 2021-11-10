# Задание 3
#
# "Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках".

import random
import statistics


def middle(m):
    arr = [random.randint(0, 10) for i in range(2 * m + 1)]
    print(arr)
    arr = sorted(arr)
    mid_idx = len(arr) // 2
    return arr[mid_idx]


print(middle(6))
# [5, 0, 6, 9, 10, 3, 1, 1, 7, 4, 8, 7, 4]
# 5


def another_middle(m):
    arr = [random.randint(0, 10) for i in range(2 * m + 1)]
    print(arr)
    return statistics.median(arr)


print(another_middle(6))
# [7, 1, 7, 5, 8, 6, 9, 8, 3, 3, 10, 10, 5]
# 7
