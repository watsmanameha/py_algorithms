# Задание 4 "Написать программу, которая генерирует в указанных пользователем границах:
# 1)случайное целое число;
# 2)случайное вещественное число;
# 3)случайный символ".

import random

symbol_type = input('Какой тип данных вы хотите получить?\n i(int), f(float), c(char)\n')
lv = input('Введите нижнюю границу\n')
uv = input('Введите верхнюю границу\n')

if symbol_type == 'i':
    out = random.randint(int(lv), int(uv))
    print(f'Случайное целое число равно {out}')
elif symbol_type == 'f':
    out = random.uniform(float(lv), float(uv))
    print(f'Случайное вещественное число равно {out}')
elif symbol_type == 'c':
    out = chr(random.randint(ord(lv), ord(uv)))
    print(f'Случайный символ: {out}')
else:
    print('Выбранный тип данных не подходит, попробуйте снова\n')