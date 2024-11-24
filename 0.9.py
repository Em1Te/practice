# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.9.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DrxDnlFvPcMGd5RWBIUEC2npY77_V0SR

ФИО
"""

Костоусов Егор Максимович

"""# Дисклеймер

В данной практике вам необходимо применить все ваши знания по темам:

- Функции
- Словари
- Списки
- Множества
- Условные конструкции
- Запросы

и все что было изучено на прошлых практических занятиях

В каждом задании кратко описаны функции, которые необходимо реализовать, детали реализации вы должны продумать самостоятельно

# Задание 0

Создайте функцию по нахождению уникальных элементов из двух списков



```
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
```
"""

def find_unique(list1, list2):
    unique_elements = set(list1).symmetric_difference(set(list2))
    return list(unique_elements)


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

unique_elements = find_unique(a, b)
print(unique_elements)

"""# Задание 1

Симулятор виртуального питомца

Цель: создать виртуальный симулятор домашних животных, в котором пользователи смогут заводить питомцев и ухаживать за ними.

Требования:

- Функция для усыновления питомца (имя, тип, возраст).
- Функция для того, чтобы покормить питомца, поиграть с ним или уложить его спать.
- Функция для отображения состояния питомца (голод, радость, энергия).

# Задание 2

Рыцарь и дракон

Цель: создать небольшую игру, в которой вам необходимо играть за рыцаря и сразиться с драконом

Требования:

- Создание персонажа (имя, информация о доспехах, оружии, урон, здоровье)
- Управление персонажем и мини сюжет
- Создание дракона (Имя, информация о здоровье и уроне)
- Боевая система (нанесение и получение урона, урон должен быть случайным в заданном диапазоне)
- Реализовать бой между драконом и рыцарем
"""

def status(name, hunger, mood, energy):
    print(f'Голод {name} = {hunger} /10')
    print(f'Настроение {name} = {mood} /10')
    print(f'Энергия {name} = {energy} /10')


def actions(hunger, mood, energy):
    action = input('Введите действие: ')
    if action == "Покормить":
        hunger += 2
        energy += 1
        mood += 1
        print('Ты покормил питомца')
    elif action == 'Играть':
        mood += 2
        energy -= 2
        hunger -= 1
        print('Ты поиграл с питомцем')
    elif action == 'Спать':
        energy += 3
        mood += 1
        hunger -= 2
        print('Ты уложил питомца спать')
    else:
        print('Некорректный ввод')
    return hunger, mood, energy


def alive(name, hunger, mood, energy):
    if hunger <= 0:
        print(f'{name} обиделся и ушёл кушать к другому')
        return False
    if mood <= 0:
        print(f'{name} стало слишком грустно, теперь у него передозировка мармеладок')
        return False
    if energy <= 0:
        print(f'{name} слишком устал и уснул на улице')
        return False
    return True


def main():
    name = input('Как вы хотите назвать своего питомца: ')
    view = input('Какой тип у вашего питомца: ')
    age = input('Сколько лет вашему питомцу: ')

    hunger = 5
    mood = 5
    energy = 5

    while True:
        status(name, hunger, mood, energy)
        hunger, mood, energy = actions(hunger, mood, energy)
        if not alive(name, hunger, mood, energy):
            break


if __name__ == "__main__":
    main()

import random


def create_knight():
    name = input('Введите имя рыцаря: ')
    armor = int(input('Введите уровень брони: '))
    weapon_damage = int(input('Введите урон(10-20): '))
    health = 100
    return {'name': name, 'armor': armor, 'weapon': 'Алмазный меч', 'health': health, 'damage': weapon_damage}


def create_dragon():
    name = 'Бульбазавр'
    health = 150
    damage = 20
    return {'name': name, 'health': health, 'damage': damage}


def attack(character):
    if 'armor' in character:
        return random.randint(int(character['damage'] * 0.8), int(character['damage'] * 1.2))
    return random.randint(int(character['damage'] * 0.8), int(character['damage'] * 1.2))


def take_damage(character, damage):
    if 'armor' in character:
        damage = max(damage - character['armor'], 0)
    character['health'] -= damage
    return damage


def is_alive(character):
    return character['health'] > 0


def battle(knight, dragon):
    print(f'{knight["name"]} отправляется в опасное путешествие, чтобы победить {dragon["name"]}"a и освободить из его лап прекрасную принцессу Потату')
    print(f'{knight["name"]} встретил {dragon["name"]} на своем пути, и началась битва!')

    while is_alive(knight) and is_alive(dragon):
        knight_damage = attack(knight)
        print(f'{knight["name"]} атакует {dragon["name"]} и наносит {knight_damage} урона.')
        take_damage(dragon, knight_damage)

        if not is_alive(dragon):
            print(f'{dragon["name"]} повержен. {knight["name"]} победил и освободил Потату)')
            break

        dragon_damage = attack(dragon)
        print(f'{dragon["name"]} атакует {knight["name"]} и наносит {dragon_damage} урона.')
        take_damage(knight, dragon_damage)

        if not is_alive(knight):
            print(f'{knight["name"]} погиб! {dragon["name"]} победил!')
            break


def main():
    knight = create_knight()
    dragon = create_dragon()
    battle(knight, dragon)


if __name__ == '__main__':
    main()

"""# Задание 3

Цель - создать менеджера команды Pokémon, который позволит пользователям:

- Добавлять покемонов в свою команду. (если такого покемона еще нет в команде)
- Удалять покемонов из их команды.
- Просматривать подробную информацию обо всех покемонах в команде.
- Находить покемона по имени.
- Устраивать тренировочный бой между двумя покемонами

Для данной задачи используйте: https://pokeapi.co/
"""

