# Задание 8
#
# "Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры".

num = int(input('Введите последовательность чисел:\n'))
digit = int(input('Введите цифру, количество которой вы хотите посчитать\n'))
quantity = 0

while num > 0:
    a = num % 10
    if digit == a:
        quantity += 1
    num //= 10

print(quantity)
