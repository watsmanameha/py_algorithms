# Задание 3 "По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y=kx+b, проходящей через эти точки".

x1, y1 = input('Введите координаты x1 и y1 первой точки:\n')
x2, y2 = input('Введите координаты x2 и y2 второй точки:\n')

x1, y1, x2, y2 = map(float, [x1, y1, x2, y2]) # Приведём полученные значения к классу float

# Имея функцию y=kx+b, найдём k и b, используя полученные от пользователя координаты

# k = (y2 - y1) / (x2 - x1),
# b = (y1 * x2 - y2 * x1) / (x2 - x1)

if x2 - x1 != 0: # Делаем проверку на область допустимых значений
    k = (y2 - y1) / (x2 - x1)
    b = (y1 * x2 - y2 * x1) / (x2 - x1)
    print(f'Полученное уравнения прямой выглядит следующим образом: y = {k} * x + {b}')
else:
    print('Error')


