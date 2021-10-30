# Задание 8
#
# "Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу".

M = 5
N = 4
matrix = []

for i in range(N):
    values_of_matrix = []
    amount = 0
    print(f'Заполните {i}-ую строку матрицы')
    for j in range(M-1):
        num = int(input())
        amount += num
        values_of_matrix.append(num)
    values_of_matrix.append(amount)
    matrix.append(values_of_matrix)

print(matrix)
