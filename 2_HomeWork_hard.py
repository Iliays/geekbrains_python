# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y
equation = 'y = -12x + 11111140.2121'
x = 2.5
y = 0
num_x = 0
string = equation.split(' ')
for x_find in string:
    if 'x' in x_find:
        num_x = x_find
        num_x = num_x[:-1]
        num_x = int(num_x)
another_num = string[-1]
if '.' in another_num:
    another_num = float(another_num)
else:
    another_num = int(another_num)
y = (num_x * x) + another_num
print(y)
print()
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
date = '16.04.1999'
test_date = date.split('.')
if len(test_date[-1]) == 4 and 1 <= int(test_date[-1]) <= 9999:
    if len(test_date[1]) == 2 and int(test_date[1]) <= 12:
        if len(test_date[0]) == 2 and int(test_date[0]) <= 31:
            print(date)
        else:
            print('Некорректная дата')
    else:
        print('Некорректная дата')
else:
    print('Некорректная дата')
