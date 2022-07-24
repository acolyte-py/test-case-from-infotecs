import os

from dir_for_help_test.app import web_calc


class TestWebCalcStart:
    def test_web_calc_start_ip_and_port(self):
        assert web_calc(
            exe_file="webcalc", command="start", ip_addr="192.168.1.1", port=8080) == print("log_start_default"), (
            "Функция, возвращает не то, что ожидалось. Команда [start] (ip) (port). Необходимо убедиться, "
            "что функция, работает корректо, при указанных (ip) (port)."
        )

    def test_web_calc_start_no_ip_and_port(self):
        assert web_calc(exe_file="webcalc", command="start") == print("log_start_ip_port"), (
            "Функция, возвращает не то, что ожидалось. Команда [start] не получает значений ip и port. Необходимо "
            "убедиться, что функция, берёт значения по умолчанию."
        )

    def test_web_calc_start_with_help(self):
        assert web_calc(exe_file="webcalc", command="start -h") == print("log_start_h"), (
            "При использование команды [start] с ключём [-h] не возвращается дополнительная информация."
        )
        assert web_calc(exe_file="webcalc", command="start --help") == print("log_start_h"), (
            "При использование команды [start] с ключём [--help] не возвращается дополнительная информация."
        )


class TestWebCalcStop:
    def test_web_calc_stop(self):
        assert web_calc(exe_file="webcalc", command="stop") == print("log_stop"), (
            "При использование команды [stop] приложение должно остановить свой процесс."
        )


class TestWebCalcRestart:
    def test_web_calc_restart_ip_and_port(self):
        assert web_calc(exe_file="webcalc", command="restart") == print("log_restart_default"), (
            "При использование команды [restart] приложение должно перезапуститься. При этом значения (ip) (port), "
            "если не были, явно указаны при использование команды [start], должны использовать значения по умолчанию "
        )

    def test_web_calc_restart_no_ip_and_port(self):
        assert web_calc(
            exe_file="webcalc", command="restart", ip_addr="192.168.1.1", port=8080) == print("log_restart_ip_port"), (
            "При использование команды [restart] приложение должно перезапуститься."
        )


class TestWebCalcShowLog:
    def test_web_calc_show_log(self):
        assert web_calc(
            exe_file="webcalc", command="show_log") == os.system("%localappdata%/webcalculator/webcalculator.log"), (
            "При использование команды [show_log] должен запуститься файл с логами приложения."
        )


class TestWebCalcHelp:
    def test_web_calc_h(self):
        assert web_calc(exe_file="webcalc", command="-h") == print("log_h_or_help"), (
            "При использование ключа [-h] должен выводится список команд приложения"
        )

    def test_web_calc_help(self):
        assert web_calc(exe_file="webcalc", command="--help") == print("log_h_or_help"), (
            "При использование ключа [--help] должен выводится список команд приложения"
        )


# class TestWebCalcErrorMoment:
#     def test_web_calc_command_error(self):
#         assert web_calc(exe_file="webcalc", command="") == print("error_log"), (
#             "Если в значение {command} попало пустое значение, необходимо извлечь ошибку"
#         )
#         assert web_calc(exe_file="webcalc", command="asdasdasd") == print("error_log"), (
#             "Если в значение {command} попало не зарегистрированное значение, необходимо извлечь ошибку"
#         )
