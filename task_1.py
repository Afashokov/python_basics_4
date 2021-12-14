"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
# Согласно статье 209 НК РФ с премии удерживаются налоги 13%.
# Источник https://www.b-kontur.ru/enquiry/453-nalogi-s-premii
from sys import argv
import datetime

try:
    file, name, surname, hours, salary_rate, premium_percentages = argv
# Заполнение: Имя Фамилия часы_работы часовой_оклад примия_в_процентах_от_месячного_оклада(например 30)
except ValueError:
    print("Invalid args. Возможно недостаточно аргументов")
    exit()

current_date = datetime.date.today()


def salary_calculation(hours, salary_rate, premium_percentages):
    salary = hours * salary_rate
    return salary * .87, (salary * (premium_percentages / 100)) * .87


try:
    pay_sheet = salary_calculation(float(hours), float(salary_rate), float(premium_percentages))
except ValueError:
    print("Invalid type. hours, salary_rate, premium_percentages должны быть числовыми значениями")
    exit()
print(f'Рассчетный лист сотрудника {name} {surname} за {current_date.month}.{current_date.year}')
print(f'Месячный оклад и премия с учетом налогов: {round(pay_sheet[0], 2)}, {round(pay_sheet[1], 2)}')
print(f'Итого: {round(sum(pay_sheet), 2)}')
