# Задание 1
#
# "Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком".

import hashlib


def substr_num_searching(s):
    substr_sum = set()
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            hs = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            substr_sum.add(hs)
    return f'В строке {s} различных подстрок {len(substr_sum)}'


print(substr_num_searching(input('Введите строку:\n')))
