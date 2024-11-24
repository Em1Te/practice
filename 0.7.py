# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.7.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d6PyeOIr7IW3vW53hc_Qd1ydyzFlTgkF

Ссылка на материалы:  [пдф тут](https://drive.google.com/file/d/16Cm2tgrpuDH8eIdxdSYyOsfDPqnJ3byd/view?usp=sharing)

ФИО:
"""

#Костоусов Егор Максимович

"""## Задание 1. HTTP-запросы, ответы и погода

Описание:

Напишите HTTP-запрос для получения информации о погоде в введенном городе из API.

Можно использовать API: https://open-meteo.com/. Используйте метод GET.


Ввод
```
56.50, 60.35
```

Вывод
```
Сегодня (1.11) погода 20 ◦С, нет осадков, туман
```
"""

pip install Fatsecret
pip install requests

# импорт библиотеки
import requests
from datetime import datetime


# функция для отправки запроса
def send_request(url):
    # отправляем запрос
    response = requests.get(url)
    # проверяем код ответа (==200?)
    if response.status_code == 200:
        # возвращаем данные
        return response.json()

# получение данных из словаря
def clear_data(data):
    # получаем дату
    current_date = datetime.today().date()
    current_date = f'{current_date.day}.{current_date.month}'
    # получаем температуру
    temperature = data['current']['temperature_2m']
    temperature_format = data['current_units']['temperature_2m']
    # получаем код погоды
    weather_code = data['current']['weather_code']
    # проверяем чему равен код погоды
    if weather_code == 2:
        weather = 'нет осадков, ясно'
    elif weather_code in [45, 48]:
        weather = 'нет осадков, туман'
    else:
        weather = 'выгляни в окно и посмотри сам'
    # формируем сообщение
    message = f'Сегодня ({current_date}) погода {temperature}{temperature_format}, {weather}'
    # возвращаем сообщение
    return message

# основная функция
def main(params):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={params[0]}&longitude={params[1]}&current=temperature_2m,weather_code&timezone=Europe%2FMoscow&forecast_days=1'
    data = send_request(url)
    message = clear_data(data)
    print(message)


# params = input('Введите координаты:').split(', ')
params = [56.50, 60.35]
main(params)

"""## Задание 2. HTTP-запросы, ответы и покемоны

**Описание:**


Создайте код программы, которая будет взаимодействовать с API, со следующим функионалом:

1. Используя метод GET, отправьте запрос на endpoint /pokemon, чтобы получить список первых 20 покемонов

2. Извлеките имена покемонов из ответа и выведите их списком

3. Введите с помощью input() название одного из покемонов


```
Имя покемона: clefairy
```



4. Отправьте GET-запрос, чтобы получить полную информацию о выбранном покемоне

5. Извлеките и выведите следующие данные о введенном покемоне:

     • Имя

     • Тип

     • Вес

     • Рост

     • Способности

Используйте PokéAPI (https://pokeapi.co/), который предоставляет информацию о покемонах, их характеристиках, типах и другую информацию.
"""

import requests

def send_pokemon(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Ошибка')
        return None

def extract_pokemon_names(pokemon_data):
    if pokemon_data:
        pokemon_names = []
        for pokemon in pokemon_data['results']:
            pokemon_names.append(pokemon['name'])
        print("Список первых 20 покемонов:")
        for name in pokemon_names:
            print(name)
    else:
        print("Данные не найдены")

def send_user_pokemon(pokemon):
    user_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        pokemon_info = user_response.json()

        name = pokemon_info.get('name', 'Неизвестно')
        types = [type_info['type']['name'] for type_info in pokemon_info.get('types', [])]
        weight = pokemon_info.get('weight', 'Неизвестно')
        height = pokemon_info.get('height', 'Неизвестно')
        abilities = [ability['ability']['name'] for ability in pokemon_info.get('abilities', [])]

        print(f"Имя: {name}")
        print(f"Тип: {', '.join(types) if types else 'Неизвестно'}")
        print(f"Вес: {weight}")
        print(f"Рост: {height}")
        print(f"Способности: {', '.join(abilities) if abilities else 'Неизвестно'}")
    else:
        print('Ошибка')
        return None

url = 'https://pokeapi.co/api/v2/pokemon?limit=20'

pokemon_data = send_pokemon(url)
extract_pokemon_names(pokemon_data)

pokemon = input('Введите имя вашего покемона на английском с маленькой буквы: ')
send_user_pokemon(pokemon)

"""## Задание 3. HTTP-запросы, ответы и посты

**Описание:**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API, реализуя следующие функции:

1. Реализуйте функцию, которая выполняет GET-запрос к https://jsonplaceholder.typicode.com/posts и возвращает список постов в формате JSON

2. Реализуйте функцию, котороая получает вводимое ID поста, выполняет GET-запрос по ID и возвращает данные поста в формате JSON

3. Реализуйте функцию, которая выполняет обработку JSON из пункта 2 и выводит всю важную информацию в консоль
"""

import requests

def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_post_by_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_post_info(post_data):
    if post_data:
        print(f"ID поста: {post_data['id']}")
        print(f"Заголовок: {post_data['title']}")
        print(f"Содержимое: {post_data['body']}")
        print(f"Автор ID: {post_data['userId']}")
    else:
        print("Данные поста отсутствуют.")

posts = get_posts()
if posts:
    print(f"Всего постов: {len(posts)}")

post_id = int(input("Введите ID поста для получения информации: "))
post_data = get_post_by_id(post_id)

display_post_info(post_data)

"""## Задание 4. HTTP-запросы, ответы и работа с постами

**Описание**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API (из предыдущего задания), реализуя новые функции:

1. Реализуйте функцию, которая принимает заголовок, содержимое и ID пользователя (информация вводится с помощью input()), выполняет POST-запрос для создания нового поста и возвращает информацию о созданном посте в формате JSON


```
Заголовок: Новый пост
Содержимое поста: Тут должно находиться содержимое нового поста...
ID пользователя: 10
```



2. Реализуйте функцию, которая принимает ID поста, новый заголовок и новое содержимое, выполняет PUT-запрос и возвращает обновлённый пост в формате JSON

3. Реализуйте функцию, которая принимает ID поста, выполняет DELETE-запрос и возвращает статус-код ответа
"""



"""## Задание 5. HTTP-запросы, ответы и пёсики

**Описание**

Создайте программу, которая будет взаимодействовать с Dog API, которая позволит получать список пород собак, вводить несколько пород и получать их фотогрфии.

Этапы:

1. Создайте функцию, которая использует метод GET и возвращает список всех пород собак в формате нумерованного списка

2. Реализуйте возможность ввода нескольких пород собак через запятую


```
african, chow, dingo
```



3. Создание функции, которая реализует запрос, возвращает и выводит изображениия собак, породы которых были введены до этого


Используйте Dog API (https://dog.ceo/dog-api/), который предоставляет информацию о породах собак и их изображения.

*Подсказка*



```
import requests
from PIL import Image
from IPython.display import display
import io

url = <____>
response = <____>
        
if response.<______> == <___>:
      image_url = response.json()['message']

res = requests.<__>(image_url)
img = Image.open(io.BytesIO(res.content))
display(img)
```
"""

import requests
from PIL import Image
from IPython.display import display
import io

def get_dog_breeds():
    url = 'https://dog.ceo/api/breeds/list/all'
    response = requests.get(url)
    if response.status_code == 200:
        breeds = response.json()['message']
        breed_list = []
        for index, breed in enumerate(breeds.keys()):
          breed_list.append(f"{index + 1}. {breed}")
        return breed_list
    else:
        print("Ошибка при получении данных о породах собак.")
        return []

def get_dog_images(breeds):
    for breed in breeds:
        url = f'https://dog.ceo/api/breed/{breed}/images/random'
        response = requests.get(url)
        if response.status_code == 200:
            image_url = response.json()['message']
            display_dog_image(image_url)
        else:
            print(f"Ошибка при получении изображения для породы: {breed}")

def display_dog_image(image_url):
    res = requests.get(image_url)
    img = Image.open(io.BytesIO(res.content))
    display(img)

    breeds = get_dog_breeds()
    print("Доступные породы собак:")
    for breed in breeds:
        print(breed)

    user_input = input("Введите породы собак через запятую: ")
    user_breeds = [breed.strip() for breed in user_input.split(',')]

    get_dog_images(user_breeds)