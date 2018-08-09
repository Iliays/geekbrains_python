key = True
while key:
    main_answer = int(input('\nВведите сложность задачи\n1 - easy\n2 - normal\n3 - hard\n'
                            '0 - Чтобы выйти!\nСтрока ввода: '))
    if main_answer == 0:
        print('Спасибо за использование программы, буду ждать Вас снова ^_^')
        key = False

    if main_answer == 1:
        second_key = True
        while second_key:
                answer = int(input('\nВведите номер задачи\n1 - Задача№1\n2 - Задача№2\n3 - Задача№3\n'
                                   '0 - Чтобы выйти!\nСтрока ввода: '))
                if answer == 0:
                    second_key = False

                elif answer == 1:
                    age = int(input('\nВведите возраст: '))
                    name = input('\nВведите имя: ')
                    print('\nВас зовут', name, 'и Вам', str(age), 'лет\n')

                elif answer == 2:
                    number = int(input('\nВведите любое число: '))
                    print('\nВы ввели', number, '\nЯ прибавил к нему 2 =', number + 2, '\n')

                elif answer == 3:
                    age = int(input('\nВведите возраст: '))
                    if age >= 18:
                        print('\nДоступ разрешен!')
                    else:
                        print('\nИзвините, пользование данным ресурсом только с 18 лет')

    elif main_answer == 2:
        second_key = True
        while second_key:
                answer = int(input('\nВведите номер задачи\n1 - Задача№1\n2 - Задача№2\n'
                                   '0 - Чтобы выйти!\nСтрока ввода: '))
                if answer == 0:
                    second_key = False

                elif answer == 1:
                    number = int(input('\nВведите любое число: '))
                    special_key = True
                    while special_key:
                        if 0 < number < 10:
                            number **= 2
                            print('\nЯ возвел его в квадрат =', number)
                            break
                        elif number == 0:
                            number = int(input('\nОй, извиняюсь, можно ввести только от 1 до 10\n'
                                               'P.S. десят не включаем :D\n'
                                               'P.S. 0 * 0 = 0 не надо так ^_^'
                                               'Попробуйте снова: '))
                        else:
                            number = int(input('\nОй, извиняюсь, можно ввести только от 1 до 10\n'
                                               'P.S. десят не включаем :D\n'
                                               'Попробуйте снова: '))

                elif answer == 2:
                    print('\nВерсия со свапом через кортеж')
                    number = int(input('\nВведите первое число: '))
                    number2 = int(input('Введите второе число: '))
                    arr = (number, number2)
                    number = arr[1]
                    number2 = arr[0]
                    print(number, number2)

                    print('\nВерсия со свапом без кортежа и без третьей переменной')
                    num = int(input('\nВведите первое число: '))
                    num2 = int(input('Введите второе число: '))
                    num, num2 = num2, num
                    print(num, num2)

    elif main_answer == 3:
        print(' ' * 10, 'Медицинская анкета')
        second_key = True
        while second_key:
            answer = int(input('\nВыберите действие\n1 - Ввести данные\n'
                               '0 - Чтобы завершить сеанс!\nСтрока ввода: '))
            if answer == 0:
                second_key = False

            elif answer == 1:
                name = input('\nВведите имя: ')
                surname = input('\nВведите фамилию: ')
                age = int(input('\nВведите возраст: '))
                weight = int(input('\nВведите вес: '))
                if age < 30 and 50 < weight < 120:
                    print(name, surname + ',', age, 'год,', 'вес', weight, '- хорошее состояние')

                elif (40 > age > 30 and weight < 50) or (40 > age > 30 and weight > 120):
                    print(name, surname + ',', age, 'год,', 'вес', weight, '- следует занятся собой')

                if (age > 40 and weight < 50) or (age > 40 and weight > 120):
                    print(name, surname + ',', age, 'год,', 'вес', weight, '- следует обратится к врачу!')
