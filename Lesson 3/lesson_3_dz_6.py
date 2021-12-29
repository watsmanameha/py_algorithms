# Задание 6
#
# "В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать"
import random

arr = [random.randint(0, 10) for i in range(10)]

min_idx, max_idx = arr.index(min(arr)), arr.index(max(arr))
direct = 1 if max_idx > min_idx else - 1

print(arr)
print(f'Минимальный элемент: {arr[min_idx]}, максимальный элемент: {arr[max_idx]}')
print(sum(arr[min_idx:max_idx:direct]) - arr[min_idx])


