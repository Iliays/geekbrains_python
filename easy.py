import shutil
import os


def make_dir(name):
    try:
        os.mkdir(name)
        print('File created')
    except:
        print("Already exist")


def remove_dir(name):
    try:
        os.removedirs(name)
        print('File created')
    except:
        print("Already exist")


def show():
    for file in os.listdir():
        print(file)


def copy():
    does = str(input('Enter: '))
    if os.path.isfile(does):
        last_file = does + ".dubl"
        try:
            shutil.copy(does, last_file)
            if os.path.exists(last_file):
                print('Создан дубликат')
        except FileExistsError:
            print('Директория с таким именем уже существует')


def open_file(name):
    os.chdir(name)
    try:
        cwd = os.getcwd()
        print('Вы успешно перешли в ', cwd)
    except(FileNotFoundError, OSError):
        print('Не верно указан путь: ', name)
