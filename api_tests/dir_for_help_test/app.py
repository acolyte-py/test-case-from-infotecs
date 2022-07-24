import os


def web_calc(exe_file, command, ip_addr=None, port=None):
    ip = "127.0.0.1"
    p = 17678
    if command == "start":
        print(f"{exe_file} запускается...")
        if ip_addr is None and port is None:
            log_start_ip_port = f"{exe_file} успешно запущен по адресу: {ip}:{p}"
            print(log_start_ip_port)
        else:
            log_start_default = f"{exe_file} успешно запущен"
            print(log_start_default)
    if command == "stop":
        print(f"{exe_file} выключается...")
        log_stop = f"{exe_file} успешно выключен"
        print(log_stop)
    if command == "restart":
        print(f"{exe_file} перезапускается...")
        if ip_addr is None and port is None:
            log_restart_ip_port = f"{exe_file} успешно перезапущен по адресу: {ip}:{p}"
            print(log_restart_ip_port)
        else:
            log_restart_default = f"{exe_file} успешно перезагружено"
            print(log_restart_default)
    if command == "show_log":
        path_to_log = os.system("%localappdata%/webcalculator/webcalculator.log")
        return path_to_log
    if command == "-h" or command == "--help":
        log_h_or_help = f"usage: {exe_file}[-h] [start, stop, restart, show_log]...\n\npositional arguments:\n" \
                        f"  (start,stop,restart,show_log)\n\t\t\t\t\tКоманды сервера:\n" \
                        f"start\t\t\t\tЗапуск сервера. Подробная подсказка: [start -h]\n" \
                        f"stop\t\t\t\tОстановка запущенного сервера\n" \
                        f"restart\t\t\t\tПерезапуск сервера\n" \
                        f"show_log\t\t\tОтображает логи сервера\n\n" \
                        f"optional arguments:\n  -h, --help\t\tshow this help message and exit\n"
        print(log_h_or_help)
    if command == "start -h" or command == "start --help":
        print(f"usage: webcalculator.exe start [-h] [host] [port]\n")
        log_start_h = f"positional arguments:\n  host\t\tАдрес, на котором будет запущен сервер. По умолчанию={ip} " \
                      f"\n  port\t\tПорт, на котором будет запущен сервер. По умолчанию={p}"
        print(log_start_h)

# else:
#     error_log = f"{exe_file}: error: argument command: invalid choice: '{command}' [choose from 'start', 'stop', " \
#                 f"'restart', 'show_log'] "
#     print(error_log)


web_calc("webcalc", "start")
