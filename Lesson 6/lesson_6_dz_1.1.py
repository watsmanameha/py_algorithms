# Задание 1
#
# "Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти".

# Windows 10 x64

# Lesson 5 dz 2
import sys

first_hex = list(input('Введите первое шестнадцатеричное число:\n'))
second_hex = list(input('Введите второе шестнадцатеричное число:\n'))

first_dec = ''.join(first_hex)
second_dec = ''.join(second_hex)

amount = list(hex(int(first_dec, 16) + int(second_dec, 16)).upper())
multiplication = list(hex(int(first_dec, 16) * int(second_dec, 16)).upper())

print(f'Сумма шестнадцатеричных чисел {first_hex} и {second_hex} равна {amount[2:]}, '
      f'произведение равно {multiplication[2:]}')

size_sum = 0
size_sum += sys.getsizeof(first_hex)
size_sum += sys.getsizeof(second_hex)
size_sum += sys.getsizeof(first_dec)
size_sum += sys.getsizeof(second_dec)
size_sum += sys.getsizeof(amount)
size_sum += sys.getsizeof(multiplication)
print(f'Занимаемый объем памяти равен {size_sum}')

# Занимаемый объем памяти равен 463
