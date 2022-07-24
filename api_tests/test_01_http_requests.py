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
        LIMIT = [-2147483648, 2147483648]

        limited_data = {
            "x": 1000,
            "y": -1000
        }

        number = list(limited_data.values())

        assert LIMIT[0] <= number[0] <= LIMIT[1], error_code_4
        assert LIMIT[0] <= number[1] <= LIMIT[1], error_code_4

    def test_no_type_int(self):
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
        type_data = {
            "x": -111,
            "y": 777
        }

        check_type = list(type_data.values())

        assert isinstance(check_type[0], int), error_code_3
        assert isinstance(check_type[1], int), error_code_3


class TestGetState:
    def test_get_base_url(self):
        response = requests.get(url=f'{SERVICE_URL}/api')
        with pytest.raises(AssertionError):
            assert response.status_code == 200, (
                "Не допустимый путь (используйте http://host:port/api/[имя_задачи])"
            )

    def test_get_state(self):
        response = requests.get(url=f"{SERVICE_URL}/api/state")
        assert response.status_code == 200, error_code_5


class TestPostAddition:

    def test_addition_bad(self):
        addition_data = {}

        response = requests.post(url=SERVICE_URL_ADDITION, data=addition_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_json

    def test_addition_good(self):
        addition_data = {
            "x": -18,
            "y": -13
        }

        response = requests.post(url=SERVICE_URL_ADDITION, data=addition_data)
        assert response.status_code == 200, error_code_json

    def test_addition_no_required_parameters(self):
        addition_data = {
            "x": -123
        }

        response = requests.post(url=SERVICE_URL_ADDITION, data=addition_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_2

    def test_addition_required_parameters(self):
        addition_data = {
            "x": 123,
            "y": 321
        }

        response = requests.post(url=SERVICE_URL_ADDITION, data=addition_data)
        assert response.status_code == 200, error_code_2


class TestPostMultiplication:

    def test_multiplication_bad(self):
        multiplication_data = {}

        response = requests.post(url=SERVICE_URL_MULTIPLICATION, data=multiplication_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_json

    def test_multiplication_good(self):
        multiplication_data = {
            "x": 670,
            "y": 20
        }

        response = requests.post(url=SERVICE_URL_MULTIPLICATION, data=multiplication_data)
        assert response.status_code == 200, error_code_json

    def test_multiplication_no_required_parameters(self):
        multiplication_data = {
            "x": -1
        }

        response = requests.post(url=SERVICE_URL_MULTIPLICATION, data=multiplication_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_2

    def test_multiplication_required_parameters(self):
        multiplication_data = {
            "x": 500,
            "y": -120
        }

        response = requests.post(url=SERVICE_URL_MULTIPLICATION, data=multiplication_data)
        assert response.status_code == 200, error_code_2


class TestPostDivision:

    def test_division_bad(self):
        division_data = {}

        response = requests.post(url=SERVICE_URL_DIVISION, data=division_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_json

    def test_division_good(self):
        division_data = {
            "x": -247534,
            "y": 234
        }

        response = requests.post(url=SERVICE_URL_DIVISION, data=division_data)
        assert response.status_code == 200, error_code_json

    def test_division_no_required_parameters(self):
        division_data = {
            "x": 333
        }

        response = requests.post(url=SERVICE_URL_DIVISION, data=division_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_2

    def test_division_required_parameters(self):
        division_data = {
            "x": 700000,
            "y": -7
        }

        response = requests.post(url=SERVICE_URL_DIVISION, data=division_data)
        assert response.status_code == 200, error_code_2


class TestPostRemainder:

    def test_remainder_bad(self):
        remainder_data = {}

        response = requests.post(url=SERVICE_URL_DIVISION, data=remainder_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_json

    def test_remainder_good(self):
        remainder_data = {
            "x": -1700,
            "y": 34
        }

        response = requests.post(url=SERVICE_URL_REMAINDER, data=remainder_data)
        assert response.status_code == 200, error_code_json

    def test_remainder_no_required_parameters(self):
        remainder_data = {
            "x": 101
        }

        response = requests.post(url=SERVICE_URL_REMAINDER, data=remainder_data)
        with pytest.raises(AssertionError):
            assert response.status_code == 400, error_code_2

    def test_remainder_required_parameters(self):
        remainder_data = {
            "x": 101010,
            "y": -1001
        }

        response = requests.post(url=SERVICE_URL_REMAINDER, data=remainder_data)
        assert response.status_code == 200, error_code_2
