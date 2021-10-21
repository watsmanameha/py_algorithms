# Задание 1 "Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь".

num = int(input('Введите трёхзначное число:\n'))

sum = 0
mul = 1

# Создадим цикл, который будет работать, пока число, заданное пользователем, не равно нулю

while num != 0:
    sum += num % 10 # Возьмём последнюю цифру числа, получив остаток от деления на 10
    mul *= num % 10
    num //= 10 # Избавимся от остатка от деления
print(f'Сумма цифр равна {sum}, произведение цифр равно {mul}')
