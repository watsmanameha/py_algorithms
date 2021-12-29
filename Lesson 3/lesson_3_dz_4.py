# Задание 4
#
# "Определить, какое число в массиве встречается чаще всего"

import random

arr = [random.randint(0, 10) for i in range(10)]

print(arr)

# print(sorted([(i, arr.count(i)) for i in set(arr)], key=lambda t: t[1])[-1])

most_frequent = None
quantity = 0

for item in arr:
    item_qty = arr.count(item) 
    if item_qty > quantity:
        quantity = item_qty
        most_frequent = item

print(f'Цифра {most_frequent} встречается {quantity} раз(а)')
