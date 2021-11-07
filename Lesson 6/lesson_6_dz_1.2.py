# Lesson 5 dz 2
import sys
import collections

companies_number = int(input('Введите количество предприятий:\n'))
companies_names = []
companies_profit = collections.defaultdict(list)

i = 1
for i in range(companies_number):
    companies_names.append(input(f'Введите наименование {i+1}-ого предприятия:\n'))
    for quarter in range(4):
        profit = int(input(f'Введите прибыль за {quarter+1} квартал:\n'))
        companies_profit[companies_names[i]].append(profit)
        quarter += 1
    quarter = 1
    i += 1

total_profit = collections.defaultdict(list)
for j in range(companies_number):
    total_profit[companies_names[j]].append(sum(companies_profit[companies_names[j]]))

total_avg = 0
for p in range(companies_number):
    total_avg += sum(total_profit[companies_names[p]]) / companies_number

print(f'Предприятия с прибылью выше среднего {total_avg}:')

for company in range(companies_number):
    if total_profit[companies_names[company]][0] >= total_avg:
        print(companies_names[company])

print(f'Предприятия с прибылью ниже среднего {total_avg}:')

for company in range(companies_number):
    if total_profit[companies_names[company]][0] <= total_avg:
        print(companies_names[company])

size_sum = 0
size_sum += sys.getsizeof(companies_number)
size_sum += sys.getsizeof(companies_names)
size_sum += sys.getsizeof(companies_profit)
size_sum += sys.getsizeof(i)
size_sum += sys.getsizeof(total_profit)
size_sum += sys.getsizeof(total_avg)
print(f'Объем занимаемой памяти равен {size_sum}')

# Объем занимаемой памяти равен 648
