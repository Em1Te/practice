# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.6.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LWO-BxBjNvWL5u9mc55UT-3-F2m-b7LQ

---

# **Дисклеймер**

В данной практике будет введен дополнительный критерий: чистота и читаемость кода, а также соблюдение правил описанных в начале практики

---

# Задание 1

**Задача:**

Напишите функцию очищающий список от дубликтов


*Запрещено:*

*   Использовать set() или готовые функции очищающие список от дубликатов

Вввод:

```
apple banana apple 1 3 4 4 5
```


Вывод:

```
apple banana 1 3 4 5
```
"""

def remove_duplicates(input_string):
    items = input_string.split()
    unique_items = []

    for item in items:
        if item not in unique_items:
            unique_items.append(item)

    return ' '.join(unique_items)

input_data = "apple banana apple 1 3 4 4 5"
output = remove_duplicates(input_data)
print(output)  # apple banana 1 3 4 5

"""# Задание 2

**Задача:**

Написать функцию для нахождения простых чисел в диапазоне

Ввод:

```
10, 50
```

Вывод:

```
11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
```
"""



"""# Задание 3

Напишите функцию для объединения двух списков (список ключей и список значении) в словарь

*Запрещено:*

*   Использования готовых функции для объединения списков (пример: zip() )

Дано:

```
keys = ['a', 'b', 'c', 'e' ]
values = [1, 2, 3, 4]
```

Вывод:
```
{'a': 1, 'b': 2, 'c': 3, 'e': 4}
```



"""

def combine(keys, values):
    result = {}
    if len(keys) < len(values):
        min_length = len(keys)
    else:
        min_length = len(values)

    for i in range(min_length):
        result[keys[i]] = values[i]

    return result


keys = ['a', 'b', 'c', 'e']
values = [1, 2, 3, 4]
print(combine(keys, values))

"""# Задание 4

Напишите функцию(ии) для подсчета статистических параметров:
*   Сумму
*   Среднее арифметическое
*   Медиану
*   Моду


*Запрещено:*

*   sum()
*   sorted()
*   и других функции предоставляющих готовое решение задания

Дано:

```
numbers = [1, 2, 2, 3, 4, 5, 6, 7, 8 ,9 ,10]

```

Вывод:
```
{'mean': 5.181818181818182, 'median': 5, 'mode': 2, 'sum': 57}
```

"""



"""# Задание 5

На ввод поступает строка символов. Строка состоит из слов, которые отделены друг от друга пробелами. Необходимо вывести самое длинное слово и его порядковый номер.

*Запрещено:*

*   len()

Дано:

```
Страдание и боль всегда обязательны для широкого сознания и глубокого сердца.

```

Вывод:
```
Самое длинное слово с номером 5: обязательны
```
"""

text = "Страдание и боль всегда обязательны для широкого сознания и глубокого сердца."
words = text.split()

max_length = 0
max_word = ""
max_index = 0

for i, word in enumerate(words, start=1):
    current_length = 0
    for symbol in word:
        current_length += 1

    if current_length > max_length:
        max_length = current_length
        max_word = word
        max_index = i


print(f"Самое длинное слово с номером {max_index}: {max_word}")

"""# Задание 6

Напишите программу, для управления оценками студентов, со следующими функциями:

* Добавление информации о студенте и его оценках.
* Подсчет среднего балла студента.
* Получение списка всех студентов с их средними баллами.
* Поиск студента по имени и вывод его оценок и среднего балла.




"""



"""# Задание 7


**Задача:**

Создайте приложение-викторину с командной строкой, которое задает пользователям вопросы по различным темам и отслеживает их результаты.

Ключевые особенности:

*   Хранение данных о вопросах и ответах на них, а также баллов за каждый вопрос
*   Реализуйте функцию для представления вопросов, принятия ответов пользователей и предоставления обратной связи о том, являются ли ответы правильными или неправильными.
*  После завершения викторины отобразите общий балл пользователя из числа ответов на вопросы.
*  Реализуйте функцию добавления нового вопроса
*  Реализуйте функцию перемешивания вопросов, для отображения случайного вопроса

"""
