# Задание 9 "Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)".

num1, num2, num3 = input('Введите три числа\n')
num1, num2, num3 = map(int, [num1, num2, num3])

if num3 > num2 > num1 or num1 > num2 > num3:
    print(f'Средним числом является {num2}')
elif num2 > num1 > num3 or num3 > num1 > num2:
    print(f'Средним числом является {num1}')
else:
    print(f'Средним числом является {num3}')