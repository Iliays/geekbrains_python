import shutil
import os
import sys


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def make_dir():
    try:
        for i in range(1, 10):
            os.mkdir("dir_" + str(i))
    except:
        print("Already exist")


def remove_dir():
    try:
        for i in range(1, 10):
            os.removedirs("dir_" + str(i))
    except:
        print("Already exist")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show():
    for file in os.listdir():
        print(file)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
