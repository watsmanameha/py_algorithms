# Задание 1
#
# "В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9".

arr = list(range(2, 100))

num_arr = [0] * 8

for el in arr:
    for num in range(2, 10):
        if el % num == 0:
            num_arr[num - 2] += 1

i = 0
while i < len(num_arr):
    print(i + 2, '-', num_arr[i])
    i += 1
