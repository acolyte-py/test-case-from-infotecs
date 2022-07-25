"""
    test_01_http_requests.py - Файл, который тестирует APi интерфейс приложения.
    Здесь я не совсем как я считаю, сделал хорошо, тут просто нужно больше практики в негативных тестах,
    и работы именно с API тестированием. Но в целом я использовал такую методику. Я бралЮ одну ветку логики,
    и тестировал её в 2 образах - Позитив/Негатив. Так же для вывода API адреса и ошибок, использовал файл
    common.py

    Использовал библиотеку pytest, для специального отлова ошибки. Так я проверял логику негативных тестов.
    Использовал библиотеку requests, для возможности сделать GET/POST запрос на API адрес
"""

import pytest
import requests

from dir_for_help_test.common import (
    SERVICE_URL,
    SERVICE_URL_ADDITION,
    SERVICE_URL_MULTIPLICATION,
    SERVICE_URL_DIVISION,
    SERVICE_URL_REMAINDER,
    error_code_json,
    error_code_5,
    error_code_4,
    error_code_3,
    error_code_2
)


class TestForCheckLimitAndType:

    def test_no_limited_parameters(self):
        """Тестируется негативный тест, лимит значения x, y"""
        LIMIT = [-2147483648, 2147483648]

        limited_data = {
            "x": 214748364800,
            "y": -214748364800
        }

        number = list(limited_data.values())

        with pytest.raises(AssertionError):
            assert LIMIT[0] <= number[0] <= LIMIT[1], error_code_4
        with pytest.raises(AssertionError):
            assert LIMIT[0] <= number[1] <= LIMIT[1], error_code_4

    def test_limited_parameters(self):
        """Тестируется позитивный тест, лимит значения x, y"""
        LIMIT = [-2147483648, 2147483648]

        limited_data = {
            "x": 1000,
            "y": -1000
        }

        number = list(limited_data.values())

        assert LIMIT[0] <= number[0] <= LIMIT[1], error_code_4
        assert LIMIT[0] <= number[1] <= LIMIT[1], error_code_4

    def test_no_type_int(self):
        """Тестируется тип значений x, y, они должны быть int. Негативный тест"""
        type_data = {
            "x": "asd",
            "y": -1.7776666
        }

        check_type = list(type_data.values())

        with pytest.raises(AssertionError):
            assert isinstance(check_type[0], int), error_code_3
        with pytest.raises(AssertionError):
            assert isinstance(check_type[1], int), error_code_3

    def test_type_int(self):
        """Тестируется тип значений x, y, они должны быть int. Позитивный тест"""
        type_data = {
            "x": -111,
            "y": 777
        }

        check_type = list(type_data.values())

        assert isinstance(check_type[0], int), error_code_3
        assert isinstance(check_type[1], int), error_code_3


class TestGetState:
    """Позитивный тест. Отправляет GET запрос на API адрес http://{you-ip}:{you-port}/api"""
    def test_get_base_url(self):
        response = requests.get(url=f'{SERVICE_URL}/api')
        with pytest.raises(AssertionError):
            assert response.status_code == 200, (
                "Не допустимый путь (используйте http://host:port/api/[имя_задачи])"
            )

    def test_get_state(self):
        """Позитивный тест. Отправляет GET запрос на API адрес http://{you-ip}:{you-port}/api/state"""
        response = requests.get(url=f"{SERVICE_URL}/api/state")
        assert response.status_code == 200, error_code_5


class TestPostAddition:

    def test_addition_bad(self):
        """Негативный тест. Если параметры x, y пустые, то при таком POST/addition запросе,
        должна вываливаться ошибка"""
        addition_data = {}

        response = requests.post(url=SERVICE_URL_ADDITION, data=addition_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_json

    def test_addition_good(self):
        """Позитивный тест. Если параметры x, y имеют int(LIMIT) значение при POST/addition запросе."""
        addition_data = {
            "x": -18,
            "y": -13
        }

        response = requests.post(url=SERVICE_URL_ADDITION, data=addition_data)
        assert response.status_code == 200, error_code_json

    def test_addition_no_required_parameters(self):
        """Негативный тест. Если при POST/addition запросе один из параметров x, y пустой"""
        addition_data = {
            "x": -123
        }

        response = requests.post(url=SERVICE_URL_ADDITION, data=addition_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_2

    def test_addition_required_parameters(self):
        """Позитивный тест. Если при POST/addition запросе все параметры x, y имеют значение.
        По сути повторение теста test_addition_good"""
        addition_data = {
            "x": 123,
            "y": 321
        }

        response = requests.post(url=SERVICE_URL_ADDITION, data=addition_data)
        assert response.status_code == 200, error_code_2


class TestPostMultiplication:

    def test_multiplication_bad(self):
        """Негативный тест. Если параметры x, y пустые, то при таком POST/multiplication запросе,
        должна вываливаться ошибка"""
        multiplication_data = {}

        response = requests.post(url=SERVICE_URL_MULTIPLICATION, data=multiplication_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_json

    def test_multiplication_good(self):
        """Позитивный тест. Если параметры x, y имеют int(LIMIT) значение при POST/multiplication запросе."""
        multiplication_data = {
            "x": 670,
            "y": 20
        }

        response = requests.post(url=SERVICE_URL_MULTIPLICATION, data=multiplication_data)
        assert response.status_code == 200, error_code_json

    def test_multiplication_no_required_parameters(self):
        """Негативный тест. Если при POST/multiplication запросе один из параметров x, y пустой"""
        multiplication_data = {
            "x": -1
        }

        response = requests.post(url=SERVICE_URL_MULTIPLICATION, data=multiplication_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_2

    def test_multiplication_required_parameters(self):
        """Позитивный тест. Если при POST/multiplication запросе все параметры x, y имеют значение.
        По сути повторение теста test_multiplication_good"""
        multiplication_data = {
            "x": 500,
            "y": -120
        }

        response = requests.post(url=SERVICE_URL_MULTIPLICATION, data=multiplication_data)
        assert response.status_code == 200, error_code_2


class TestPostDivision:

    def test_division_bad(self):
        """Негативный тест. Если параметры x, y пустые, то при таком POST/division запросе,
        должна вываливаться ошибка"""
        division_data = {}

        response = requests.post(url=SERVICE_URL_DIVISION, data=division_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_json

    def test_division_good(self):
        """Позитивный тест. Если параметры x, y имеют int(LIMIT) значение при POST/division запросе."""
        division_data = {
            "x": -247534,
            "y": 234
        }

        response = requests.post(url=SERVICE_URL_DIVISION, data=division_data)
        assert response.status_code == 200, error_code_json

    def test_division_no_required_parameters(self):
        """Негативный тест. Если при POST/division запросе один из параметров x, y пустой"""
        division_data = {
            "x": 333
        }

        response = requests.post(url=SERVICE_URL_DIVISION, data=division_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_2

    def test_division_required_parameters(self):
        """Позитивный тест. Если при POST/division запросе все параметры x, y имеют значение.
        По сути повторение теста test_division_good"""
        division_data = {
            "x": 700000,
            "y": -7
        }

        response = requests.post(url=SERVICE_URL_DIVISION, data=division_data)
        assert response.status_code == 200, error_code_2


class TestPostRemainder:

    def test_remainder_bad(self):
        """Негативный тест. Если параметры x, y пустые, то при таком POST/remainder запросе,
        должна вываливаться ошибка"""
        remainder_data = {}

        response = requests.post(url=SERVICE_URL_DIVISION, data=remainder_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_json

    def test_remainder_good(self):
        """Позитивный тест. Если параметры x, y имеют int(LIMIT) значение при POST/remainder запросе."""
        remainder_data = {
            "x": -1700,
            "y": 34
        }

        response = requests.post(url=SERVICE_URL_REMAINDER, data=remainder_data)
        assert response.status_code == 200, error_code_json

    def test_remainder_no_required_parameters(self):
        """Негативный тест. Если при POST/remainder запросе один из параметров x, y пустой"""
        remainder_data = {
            "x": 101
        }

        response = requests.post(url=SERVICE_URL_REMAINDER, data=remainder_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_2

    def test_remainder_required_parameters(self):
        """Позитивный тест. Если при POST/remainder запросе все параметры x, y имеют значение.
        По сути повторение теста test_remainder_good"""
        remainder_data = {
            "x": 101010,
            "y": -1001
        }

        response = requests.post(url=SERVICE_URL_REMAINDER, data=remainder_data)
        assert response.status_code == 200, error_code_2
