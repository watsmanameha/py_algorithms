# Задание 2
#
# "Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]".

first_hex = list(input('Введите первое шестнадцатеричное число:\n'))
second_hex = list(input('Введите второе шестнадцатеричное число:\n'))

first_dec = ''.join(first_hex)
second_dec = ''.join(second_hex)

amount = list(hex(int(first_dec, 16) + int(second_dec, 16)).upper())
multiplication = list(hex(int(first_dec, 16) * int(second_dec, 16)).upper())

print(f'Сумма шестнадцатеричных чисел {first_hex} и {second_hex} равна {amount[2:]}, '
      f'произведение равно {multiplication[2:]}')
