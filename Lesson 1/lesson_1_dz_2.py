# Задание 2
# "Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат".

a = 5
b = 6

# Операция НЕТ
print('НЕ a =', ~a)
print('НЕ b =', ~b)
# Любой бит чисел a и b изменяется на противоположный, происходит смещение чисел на -1

# Операция И
print('a И b =', a & b)
print('b И a =', b & a)

# Операция исключающее ИЛИ
print('a XOR b =', a ^ b)
print('b XOR b =', b ^ a)

# Операция ИЛИ
print('a OR b =', a | b)
print('b OR a =', b | a)

# Сдвиг влево и вправо на два знака
print('Сдвиг a влево на 2 знака =', a << 2, '; Сдвиг a вправо на 2 знака =', a >> 2)
print('Сдвиг b влево на 2 знака =', b << 2, '; Сдвиг b вправо на 2 знака =', b >> 2)
# Сдвиг влево - умножение на 2 в указанной степени, Сдвиг влево - целочисленное деление на 2 в указанной степени
