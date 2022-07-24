SERVICE_URL = "http://localhost:5413"
SERVICE_URL_ADDITION = f"{SERVICE_URL}/api/addition"
SERVICE_URL_MULTIPLICATION = f"{SERVICE_URL}/api/multiplication"
SERVICE_URL_DIVISION = f"{SERVICE_URL}/api/division"
SERVICE_URL_REMAINDER = f"{SERVICE_URL}/api/remainder"


error_code_1 = {
    "statusCode": 1,
    "statusMessage": "Ошибка вычисления"
}
error_code_2 = {
    "statusCode": 2,
    "statusMessage": "Не указаны необходимые параметры"
}
error_code_3 = {
    "statusCode": 3,
    "statusMessage": "Значения параметров должны быть целыми"
}
error_code_4 = {
    "statusCode": 4,
    "statusMessage": "Превышены максимальные значения параметров"
}
error_code_5 = {
    "statusCode": 5,
    "statusMessage": "Не верное имя задачи или тип HTTP запроса"
}
error_code_json = {
    "statusCode": 5,
    "statusMessage": "Не допустимый формат json"
}


# def create_addition_func(user_client):
#     result = []
#     data = {
#         "x": int(255),
#         "y": int(750)
#     }
#     result.append(data)
#     user_client.post('api/addition/', data=data)
#     data = {
#         "x": int(777666),
#         "y": int(-7766)
#     }
#     user_client.post('api/addition/', data=data)
#     result.append(data)
#     return result
