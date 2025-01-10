# Импорт модуля configuration, который содержит настройки подключения и путь к документации
import configuration
# Импорт модуля requests, предназначенный для отправки HTTP-запросов и взаимодействия с веб-сервисами
import requests 
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data  


        ### 1-я функция создания нового заказа

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
# json=body используется для отправки данных заказа в формате JSON
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

# Вызов функции post_new_order с телом запроса для создания нового заказа из модуля data
response = post_new_order(data.order_body)

# Вывод полученного тела ответа в формате JSON в консоль для наглядности.
# print(response.json())

# Вывод HTTP-статус кода ответа на запрос
# print(response.status_code)

# Определение переменной, содержащей трек-номер заказа из функции Создания заказа
order_track = response.json()["track"]

# Вывод трек-номера для наглядности
# print(order_track)


        ### 2-я функция для получения данных о заказе трек-номеру

# Определение функции get_new_order для отправки GET-запроса на получение данных о заказе
def get_new_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "?t=" + str(order_track))

# Вызов функции get_new_order для отправки GET-запроса
# response = get_new_order()

# Вывод HTTP-статус кода ответа на запрос
# print(response.status_code)

# Вывод ответа для наглядности
# print(response)
