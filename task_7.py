"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from math import factorial

print('1-й вариант - без "from math import factorial"')
n = input('Введите целое число n, будут выведены факториалы чисел до n включительно >>> ')
if n.isdigit():
    n = int(n)
else:
    print('Некорректный ввод')
    exit()


def factorial_func(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
        yield result


print(factorial_func(n))
counter = 1
for el in factorial_func(n):
    print(f'факториал числа {counter} = {el}')
    counter += 1
print('2-й вариант - c "from math import factorial"')


def fact(n):
    for num in range(1, n + 1):
        yield factorial(num)


counter = 1
print(fact(n))
for el in fact(n):
    print(f'факториал числа {counter} = {el}')
    counter += 1
