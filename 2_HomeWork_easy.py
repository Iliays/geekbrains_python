# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
arr = ['apple', 'orange', 'pineapple', 'banana']
count = 1
for fruits in arr:
    res = f'{count}. {fruits.rjust(10)}'
    count += 1
    print(res)
print()
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
arr = ['apple', 'orange', 'pineapple', 'banana']
arr2 = ['apple', 'banana', 'python']
for fruits in arr:
    if fruits in arr2:
        arr.remove(fruits)
print(arr)
print()

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
arr = [12, 20, 31, 34, 75]
for numbers in range(len(arr)):
    if arr[numbers] % 2 == 1:
        arr[numbers] *= 2
    else:
        arr[numbers] //= 4
print(arr)
