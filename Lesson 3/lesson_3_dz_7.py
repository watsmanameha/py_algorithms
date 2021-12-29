# Задание 7
#
# "В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться."
import random

arr = [random.randint(0, 20) for i in range(10)]
print(arr)

arr = sorted(arr)
print(arr)

print(arr[:2])


