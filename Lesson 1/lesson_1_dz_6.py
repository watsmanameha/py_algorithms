# Задание 6 "Пользователь вводит номер буквы в алфавите. Определить, какая это буква"

letter_num = int(input('Введите номер буквы в алфавите:\n'))

if letter_num > 1 ^ letter_num < 26:
    letter_num = ord('a') + letter_num - 1
    print('Это буква:', chr(letter_num))
else:
    print('Введите цифру от 1 до 26')
