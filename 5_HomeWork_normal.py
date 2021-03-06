# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
#
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import easy

person = int(input('1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку'
                   '\nВведите: '))
if person == 1:
    name = input('Enter the way to file: ')
    easy.open_file(name)
elif person == 2:
    easy.show()
elif person == 3:
    name = input('Enter name of file: ')
    easy.remove_dir(name)
else:
    name = input('Enter name of file: ')
    easy.make_dir(name)
