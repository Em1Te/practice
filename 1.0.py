# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 1.0.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uzrhypOJ9VRIuHa3MmnVxeigBcrlLwDF

ФИО:

Костоусов Егор Максимович

# Задание (совместное с преподавателем)

Напишите систему для учёта отпусков с возможностью узнавать, сколько дней отпуска осталось у того или иного сотрудника.
Для этого создайте класс Employee со следующими методами:

- Метод consume_vacation должен отвечать за списание дней отпуска.

Единственный параметр этого метода (кроме self) — количество потраченных отпускных дней (целое число).

При вызове метода consume_vacation соответствующее количество дней должно вычитаться из общего числа доступных отпускных дней сотрудника.

Чтобы определить число доступных отпускных дней конкретного сотрудника, в классе опишите атрибут экземпляра |, который по умолчанию будет равен значению атрибута класса vacation_days, и используйте этот атрибут в работе метода.

- Метод get_vacation_details должен возвращать остаток отпускных дней сотрудника в формате: ```Остаток отпускных дней: <число>.```


Чтобы проверить работу программы:
1. Создайте экземпляр класса Employee.
2. Вызовите метод consume_vacation, указав подходящее значение аргумента, например 7.
3. Вызовите метод get_vacation_details.
"""

class Employee:
    # количество дней отпуска, атрибут для каждого объекта класса
    vacation_days = 28

    def __init__(self, first_name, second_name, gender, amount_of_limbs):
        self.first_name = first_name # имя
        self.second_name = second_name # фамилия
        self.gender = gender # пол
        self.remaining_vacation_days = self.vacation_days # количество доступных дней отпуска


    # вычитание отгуляных дней
    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    # Вывод информации об отпуске
    def vacation_details(self):
        return f"Остаток отпускных дней: {self.remaining_vacation_days}."


employee = Employee('Олег', "Крутой", "м", "4")
employee2 = Employee('Олег', "не очень Крутой", "м", "3")
print('='*20,'\n',
      employee.first_name,'\n',
      employee.second_name,'\n',
      employee.remaining_vacation_days,'\n',
      '='*20,'\n'
      )

print('='*20,'\n',
      employee2.first_name,'\n',
      employee2.second_name,'\n',
      employee2.remaining_vacation_days,'\n',
      '='*20,'\n'
      )

"""# Задание 1

Задание:

Создайте класс с именем Rectangle который имеет:
- Атрибуты ширины и высоты.
- Метод расчета площади.
- Метод расчета периметра.
- Метод отображения размеров прямоугольника.

Создайте экземпляр класса Rectangleи продемонстрируйте его функциональность.
"""

class Rectrangle:
    def __init__(self, width, length):
        self.width = width
        self.lenght = length

    def area_calculation(self):
        return self.width * self.lenght

    def perimeter_calculation(self):
        return 2 * self.width + 2 * self.lenght

    def print_size(self):
        return f'Высота: {self.lenght}, Ширина: {self.width}'

    def change_size(self, result_length, result_wight):
        self.lenght = new_length
        self.width = new_wight

first = int(input('Введите ширину:'))
second = int(input('Введите длину:'))
result = Rectrangle(first, second)
print(result.area_calculation())
print(result.perimeter_calculation())
print(result.print_size())

"""3# Задание 2

Задание: Создайте мини версию банковской системы:


Инструкции:

1. Создайте класс BankAccountсо следующими атрибутами:
    - account_holder -  владелец счета
    - balance - баланс счета

2. Реализуйте следующие методы:
    - Метод для инициализации владельца счета: имя владельца счета и установите начальный баланс на 0.
    - deposit(amount): Добавьте указанную сумму к балансу.
    - withdraw(amount): Вычесть указанную сумму из баланса, если средств достаточно; в противном случае вывести предупреждение.
    - get_balance(): Возврат текущего баланса.


Создайте объект класса и продемонстрируйте его возможности
"""

class BankAccountco:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f'Балланс пополнен на {amount}'


    def withdraw(self, amount):
        if self.balance < amount:
            return f'У вас не хватате денег на баллансе'
        else:
            self.balance -= amount
            return f'С вашего балланса снято {amount}'


    def get_balance(self):
        return f"Текущий балланс: {self.balance}"


account_holder = input("Введите имя владельца счёта: ")
account = BankAccountco(account_holder)

while True:
    print("\nВыберите действие:")
    print("1. Пополнить баланс")
    print("2. Снять средства")
    print("3. Проверить баланс")
    print("4. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        amount = float(input("Введите сумму для пополнения: "))
        print(account.deposit(amount))
    elif choice == "2":
        amount = float(input("Введите сумму для снятия: "))
        print(account.withdraw(amount))
    elif choice == "3":
        print(account.get_balance())
    elif choice == "4":
        print("Выход из программы. До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

"""# Задание 3

Возьмите код и задание (Рыцарь и дракон) из предыдущей практики и реализуйте его с применением классов
"""

import random


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        return random.randint(int(self.damage * 0.8), int(self.damage * 1.2))

    def take_damage(self, damage):
        self.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0


class Knight(Character):
    def __init__(self, name, armor, damage):
        Character.__init__(self, name, health=100, damage=damage)
        self.armor = armor
        self.weapon = 'Алмазный меч'

    def take_damage(self, damage):
        reduced_damage = max(damage - self.armor, 0)
        self.health -= reduced_damage
        return reduced_damage


class Dragon(Character):
    def __init__(self):
        Character.__init__(self, name='Бульбазавр', health=150, damage=20)


class Battle:
    def __init__(self, knight, dragon):
        self.knight = knight
        self.dragon = dragon

    def start(self):
        print(f'{self.knight.name} отправляется в опасное путешествие, чтобы победить {self.dragon.name} и освободить прекрасную принцессу Потату.')
        print(f'{self.knight.name} встретил {self.dragon.name} на своем пути, и началась битва!')

        while self.knight.is_alive() and self.dragon.is_alive():
            knight_damage = self.knight.attack()
            print(f'{self.knight.name} атакует {self.dragon.name} и наносит {knight_damage} урона.')
            self.dragon.take_damage(knight_damage)

            if not self.dragon.is_alive():
                print(f'{self.dragon.name} повержен. {self.knight.name} победил и освободил Потату!')
                break

            dragon_damage = self.dragon.attack()
            print(f'{self.dragon.name} атакует {self.knight.name} и наносит {dragon_damage} урона.')
            reduced_damage = self.knight.take_damage(dragon_damage)
            print(f'{self.knight.name} блокировал {dragon_damage - reduced_damage} урона своей броней.')

            if not self.knight.is_alive():
                print(f'{self.knight.name} погиб! {self.dragon.name} победил!')
                break


def main():
    knight_name = input('Введите имя рыцаря: ')
    knight_armor = int(input('Введите уровень брони: '))
    knight_damage = int(input('Введите урон (10-20): '))
    knight = Knight(name=knight_name, armor=knight_armor, damage=knight_damage)

    dragon = Dragon()

    battle = Battle(knight, dragon)
    battle.start()


if __name__ == '__main__':
    main()

"""# Дополнительное задание

Задача: Система управления библиотекой

**Цель**
Создайте простую систему управления библиотекой, которая позволит пользователям добавлять книги, брать книги, возвращать книги и просматривать список доступных книг.

**Требования**

1. **Определение класса**:
   – Создайте класс с именем «Book» со следующими атрибутами:
     - `title`
     - `автор`
     - `isbn`
     - `is_borrowed` (по умолчанию `False`)

2. **Класс библиотеки**:
   - Создайте класс с именем Library, который управляет коллекцией книг.
   - Класс должен иметь следующие методы:
     - `__init__(self)`: инициализирует пустой список книг.
     - `add_book(self, book: Book)`: добавляет новую книгу в библиотеку.
     - `borrow_book(self, isbn: str)`: помечает книгу как заимствованную. Если книга не найдена или уже взята, выведите соответствующее сообщение.
     - `return_book(self, isbn: str)`: помечает книгу как возвращенную. Если книга не найдена или не была взята взаймы, выведите соответствующее сообщение.
     - `list_available_books(self)`: печатает список всех доступных книг в библиотеке.
     - `find_book(self, isbn: str)`: возвращает объект книги, если он найден, в противном случае возвращает `None`.

3. **Взаимодействие с пользователем**:
   - Создайте простое текстовое меню, которое позволит пользователям:
     - Добавить книгу
     - Одолжить книгу
     - Вернуть книгу
     - Список доступных книг
     - Выйти из программы
"""