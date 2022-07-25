"""
    test_02_calculator.py - Позитивные тесты для расчётов.
    В качестве каркаса используются функции из файла: "calculator.py".
    Основная логика, я брал определённые параметры. Параметры выбирались дабы максимально проверить возможные
    исключение в расчётах, например с 0 или - отрицательные числа.

    Использовал библиотеку pytest для марки parametrize, чтобы одна тест функция брала несколько значений для теста
"""

import pytest

from dir_for_help_test.calculator import addition, multiplication, division, remainder
from dir_for_help_test.common import error_code_1


class TestAddition:
    """TestAddition - проверяет правильность расчётов функции [addition] (сложение)"""
    param = [
        (778899, 224411, 1003310),
        (-1414, -5523, -6937),
        (-254, 999, 745),
        (777777, 0, 777777),
        (123123, 456456, 579579)
    ]

    @pytest.mark.parametrize("x, y, result", param)
    def test_addition_good(self, x, y, result):
        assert addition(x, y) == result, error_code_1


class TestMultiplication:
    """TestMultiplication - проверяет правильность расчётов функции [multiplication] (умножение)"""
    param = [
        (540, 0, 0),
        (-320, -290, 92800),
        (7000, -100, -700000),
        (4560, 72, 328320),
        (12, 2, 24)
    ]

    @pytest.mark.parametrize("x, y, result", param)
    def test_multiplication_good(self, x, y, result):
        assert multiplication(x, y) == result, error_code_1


class TestDivision:
    """TestDivision - проверяет правильность расчётов функции [division] (деление)"""
    param = [
        (10, 5, 2),
        (100, 50, 2),
        (100, -10, -10),
        (2000000, 2000, 1000),
        (-6000000, 1250, -4800)
    ]

    @pytest.mark.parametrize("x, y, result", param)
    def test_division_good(self, x, y, result):
        assert division(x, y) == result, error_code_1


class TestRemainder:
    """TestRemainder - проверяет правильность расчётов функции [remainder] (остаток от деления)"""
    param = [
        (-1000, 7, 1),
        (56001, -78, -3),
        (-998, -77, -74),
        (777661, 111991, 105715),
        (69, 1, 0)
    ]

    @pytest.mark.parametrize("x, y, result", param)
    def test_remainder_good(self, x, y, result):
        assert remainder(x, y) == result, error_code_1
