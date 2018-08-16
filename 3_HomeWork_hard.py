# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
import random

player = {'name': input('Enter name of player: '), 'health': random.randint(50, 150), 'damage': random.randint(10, 40)}
enemy = {'name': input('Enter name of enemy: '), 'health': random.randint(50, 150), 'damage': random.randint(10, 40)}
print(f'Созданы игроки: {player} и '
      f'{enemy}')

def attack(person1, person2):
    person2['health'] = person2['health'] - person1['damage']
    return person2['health']

while player['health'] > 0 and enemy['health'] > 0:
    count = random.randint(1, 2)
    if count == 1:
        start = attack(player, enemy)
        print(f'Урон нанесен игроку {enemy["name"]} : {enemy["health"]}')
    else:
        start = attack(enemy, player)
        print(f'Урон нанесен игроку {player["name"]} : {player["health"]}')

if player['health'] > enemy['health']:
    print(f'Победил игрок с именем : {player["name"]}, здоровья осталось : {player["health"]}')
elif player['health'] < enemy['health']:
    print(f'Победил игрок с именем : {enemy["name"]}, здоровья осталось : {enemy["health"]}')
elif player['health'] == enemy['health']:
    print(f'Ничья! Игроки : имя {enemy["name"]}, здоровье {enemy["health"]}'
          f'имя {player["name"]}, здоровье {player["health"]}')

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
def save(person):
    with open(person['name'] + '.txt', 'w', encoding='utf-8') as file:
        file.write(f'Name {person["name"]}\n')
        file.write(f'Health {person["health"]}\n')
        file.write(f'Damage {person["damage"]}\n')
        file.write(f'Armor {person["armor"]}')


player = {'name': input('Enter name of player: '), 'health': random.randint(50, 150), 'damage': random.randint(10, 40),
          'armor': random.randint(1, 5)}
enemy = {'name': input('Enter name of enemy: '), 'health': random.randint(50, 150), 'damage': random.randint(10, 40),
         'armor': random.randint(1, 5)}
print(f'Созданы игроки: {player} и {enemy}')

save(player)
save(enemy)

def read(person):
    new = {}
    j = []
    with open(person['name'] + '.txt', 'r', encoding='utf-8') as file:
        for i in file:
            j.append(i.split())
    if j[1][0] == 'Name':
        new['name'] = int(j[1][1])
    elif j[1][0] == 'Health':
        new['health'] = int(j[1][1])
    elif j[1][0] == 'Damage':
        new['damage'] = int(j[1][1])
    elif j[1][0] == 'Armor':
        new['armor'] = int(j[1][1])
    return new


read(player)
read(enemy)

def armor(person1, person2):
    damage = person1['damage'] // person2['armor']
    return damage

def damage(person2, damage):
    person2['health'] = person2['health'] - damage
    return person2['health']

while player['health'] > 0 and enemy['health'] > 0:
    count = random.randint(1, 2)
    if count == 1:
        start = armor(player, enemy)
        last = damage(enemy, start)
        print(f'Урон нанесен игроку {enemy["name"]} : {enemy["health"]}')
    else:
        start = armor(enemy, player)
        last = damage(player, start)
        print(f'Урон нанесен игроку {player["name"]} : {player["health"]}')

if player['health'] > enemy['health']:
    print(f'Победил игрок с именем : {player["name"]}, здоровья осталось : {player["health"]}')
elif player['health'] < enemy['health']:
    print(f'Победил игрок с именем : {enemy["name"]}, здоровья осталось : {enemy["health"]}')
elif player['health'] == enemy['health']:
    print(f'Ничья! Игроки : имя {enemy["name"]}, здоровье {enemy["health"]}'
          f'имя {player["name"]}, здоровье {player["health"]}')




