# -*- coding: utf-8 -*-

"""
Задание 22.2

Создать класс CiscoTelnet, который подключается по Telnet к оборудованию Cisco.

При создании экземпляра класса, должно создаваться подключение Telnet, а также
переход в режим enable.
Класс должен использовать модуль telnetlib для подключения по Telnet.

У класса CiscoTelnet, кроме __init__, должно быть, как минимум, два метода:
* _write_line - принимает как аргумент строку и отправляет на оборудование строку
  преобразованную в байты и добавляет перевод строки в конце. Метод _write_line должен
  использоваться внутри класса.
* send_show_command - принимает как аргумент команду show и возвращает вывод
  полученный с обрудования

Параметры метода __init__:
* ip - IP-адрес
* username - имя пользователя
* password - пароль
* secret - пароль enable

Пример создания экземпляра класса:
In [2]: from task_22_2 import CiscoTelnet

In [3]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}
   ...:

In [4]: r1 = CiscoTelnet(**r1_params)

In [5]: r1.send_show_command("sh ip int br")
Out[5]: 'sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up      
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up      
Ethernet0/2                unassigned      YES manual up                    up      
Ethernet0/3                192.168.130.1   YES NVRAM  up                    up      
R1#'


Подсказка:
Метод _write_line нужен для того чтобы можно было сократить строку:
self.telnet.write(line.encode("utf-8") + b"
")

до такой:
self._write_line(line)

Он не должен делать ничего другого.
"""

import time
import telnetlib
import yaml


class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self._write_line(username)
        self.telnet.read_until(b"Password:")
        self._write_line(password)
        self._write_line("enable")
        self.telnet.read_until(b"Password:")
        self._write_line(secret)
        self._write_line("terminal length 0")
        time.sleep(1)
        self.telnet.read_very_eager()

    def _write_line(self, line):
        self.telnet.write(line.encode("utf-8") + b"\n")

    def send_show_command(self, command):
        self._write_line(command)
        command_output = self.telnet.read_until(b"#").decode("utf-8")
        return command_output


if __name__ == "__main__":
    r1_params = {
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    r1 = CiscoTelnet(**r1_params)
    print(r1.send_show_command("sh ip int br"))
