# Кристина Пюльзю, 25А-я когорта — Финальный проект. Инженер по тестированию плюс

# Импорт модуля sender_stand_request, содержащий функции для отправки HTTP-запросов к API
import sender_stand_request
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


# Шаг 1. Тест запроса на создание заказа c исходными данными data

# Определение теста test_create_new_order для отправки POST-запроса на создание нового заказа
def test_create_new_order():
    order_responce = sender_stand_request.post_new_order(data.order_body)
    assert order_responce.status_code == 201
    assert order_responce.json()["track"] != ""
    

# Шаг 2. Запрос на получение данных для нового заказа

# Определение теста test_get_order_data для отправки GET-запроса
def test_get_order_data():
    get_responce = sender_stand_request.get_new_order()
    assert get_responce.status_code == 200
