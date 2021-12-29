# Задание 2
#
# "Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Проанализировать скорость и сложность алгоритмов".

import cProfile

# Без использования "Решета"


def common_numbers(n):
    primes = list(range(2, n + 1))

    for i in primes:
        for elem in primes:
            if elem % i == 0 and elem != i:
                primes.remove(elem)
    return primes

# С использованием "Решета"


def eratosthenes(n):
    primes = list(range(2, n + 1))

    for i in primes:
        if i != 0:
            for j in range(2 * i, n + 1, i):
                primes[j - 2] = 0
    return list(filter(lambda x: x != 0, primes))


cProfile.run('common_numbers(10)')
#  9 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_dz_2.py:13(common_numbers)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         5    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
cProfile.run('common_numbers(100)')
# 78 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_dz_2.py:13(common_numbers)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        74    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
cProfile.run('common_numbers(1000)')
# 835 function calls in 0.008 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#         1    0.003    0.003    0.008    0.008 lesson_4_dz_2.py:13(common_numbers)
#         1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       831    0.005    0.000    0.005    0.000 {method 'remove' of 'list' objects}
cProfile.run('eratosthenes(10)')
# 13 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_dz_2.py:25(eratosthenes)
#         9    0.000    0.000    0.000    0.000 lesson_4_dz_2.py:32(<lambda>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('eratosthenes(100)')
# 103 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_dz_2.py:25(eratosthenes)
#        99    0.000    0.000    0.000    0.000 lesson_4_dz_2.py:32(<lambda>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('eratosthenes(1000)')
# 1003 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 lesson_4_dz_2.py:25(eratosthenes)
#       999    0.000    0.000    0.000    0.000 lesson_4_dz_2.py:32(<lambda>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Алгоритм с "Решетом Эратосфена" оказался в 8 раз быстрее

