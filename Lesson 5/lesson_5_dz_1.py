# Задание 1
#
# "Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего".
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
