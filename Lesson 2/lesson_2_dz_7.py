# Задание 7
#
# "Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число".

print('Существует равенство "1+2+...+n = n(n+1)/2"')
n = int(input('Введите n:\n'))
sum = 0

for i in range(1, (n + 1)):
    sum += i

print('1 + 2 + ... + n =', sum)

print(f'{n * (n + 1) / 2 = }')

