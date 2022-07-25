"""
    test_03_app_functionality.py - Файл, который тестирует управление приложением.
    В качестве каркаса использую функцию [web_calc] которая описана в файле app.py
    Здесь я тестировал функциональность и поведение (command) start/stop и т. д.

    Использовал библиотеку os для возможности вывести логи приложение.
"""

import os

from dir_for_help_test.app import web_calc


class TestWebCalcStart:
    def test_web_calc_start_ip_and_port(self):
        """Тестируется ветка логики, в которой явно были указаны ip_addr и port"""
        assert web_calc(
            exe_file="webcalc", command="start", ip_addr="192.168.1.1", port=8080) == print("log_start_default"), (
            "Функция, возвращает не то, что ожидалось. Команда [start] (ip) (port). Необходимо убедиться, "
            "что функция, работает корректо, при указанных (ip) (port)."
        )

    def test_web_calc_start_no_ip_and_port(self):
        """Тестируется ветка логики, в которой не были явно указаны ip_addr и port. Если они не были явно указаны,
        то функция должна взять значения по умолчанию """
        assert web_calc(exe_file="webcalc", command="start") == print("log_start_ip_port"), (
            "Функция, возвращает не то, что ожидалось. Команда [start] не получает значений ip и port. Необходимо "
            "убедиться, что функция, берёт значения по умолчанию."
        )

    def test_web_calc_start_with_help(self):
        """Данный тест проверяет ключ [-h][--help] с командой [start], по сути он должен познакомить с параметрами
        ip и port"""
        assert web_calc(exe_file="webcalc", command="start -h") == print("log_start_h"), (
            "При использование команды [start] с ключём [-h] не возвращается дополнительная информация."
        )
        assert web_calc(exe_file="webcalc", command="start --help") == print("log_start_h"), (
            "При использование команды [start] с ключём [--help] не возвращается дополнительная информация."
        )


class TestWebCalcStop:
    def test_web_calc_stop(self):
        """Тестируется ветка остановки приложения командой [stop]"""
        assert web_calc(exe_file="webcalc", command="stop") == print("log_stop"), (
            "При использование команды [stop] приложение должно остановить свой процесс."
        )


class TestWebCalcRestart:
    def test_web_calc_restart_ip_and_port(self):
        """Тестируется команда [restart], должна перезапустить приложение, с параметрами ip_addr и port
        если они явно не были указаны, параметры должны быть по умолчанию"""
        assert web_calc(exe_file="webcalc", command="restart") == print("log_restart_default"), (
            "При использование команды [restart] приложение должно перезапуститься. При этом значения (ip) (port), "
            "если не были, явно указаны при использование команды [start], должны использовать значения по умолчанию "
        )

    def test_web_calc_restart_no_ip_and_port(self):
        """Тестируется команда [restart], должна перезапустить приложение, с параметрами ip_addr и port"""
        assert web_calc(
            exe_file="webcalc", command="restart", ip_addr="192.168.1.1", port=8080) == print("log_restart_ip_port"), (
            "При использование команды [restart] приложение должно перезапуститься."
        )


class TestWebCalcShowLog:
    def test_web_calc_show_log(self):
        """Тестируется использовании команды [show_log], необходимо получить .txt файл с логами приложения"""
        assert web_calc(
            exe_file="webcalc", command="show_log") == os.system("%localappdata%/webcalculator/webcalculator.log"), (
            "При использование команды [show_log] должен запуститься файл с логами приложения."
        )


class TestWebCalcHelp:
    def test_web_calc_h(self):
        """Тестируем функциональность ключа [-h]"""
        assert web_calc(exe_file="webcalc", command="-h") == print("log_h_or_help"), (
            "При использование ключа [-h] должен выводится список команд приложения"
        )

    def test_web_calc_help(self):
        """Тестируем функциональность ключа [--help]"""
        assert web_calc(exe_file="webcalc", command="--help") == print("log_h_or_help"), (
            "При использование ключа [--help] должен выводится список команд приложения"
        )


# class TestWebCalcErrorMoment:
#     def test_web_calc_command_error(self):
#         """Данный тест проверяет, если на вход (command) поступило пустое значение или не зарегистрированное значение
#         функция должна вернуть ошибку"""
#         assert web_calc(exe_file="webcalc", command="") == print("error_log"), (
#             "Если в значение {command} попало пустое значение, необходимо извлечь ошибку"
#         )
#         assert web_calc(exe_file="webcalc", command="asdasdasd") == print("error_log"), (
#             "Если в значение {command} попало не зарегистрированное значение, необходимо извлечь ошибку"
#         )
