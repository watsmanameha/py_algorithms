# Задание 9
#
# "Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр".

num1 = int(input('Введите первое натуральное число:\n'))
num2 = int(input('Введите второе натуральное число:\n'))
num3 = int(input('Введите третье натуральное число:\n'))

sum = 0

if num2 < num1 and num3 < num1:
    biggest_num = num1
elif num2 < num3 and num1 < num3:
    biggest_num = num3
else:
    biggest_num = num2

print(f'Наибольшее число = {biggest_num}')

while biggest_num > 0:
    digit = biggest_num % 10
    sum += digit
    biggest_num //= 10

print(f'Сумма его цифр равна {sum}')