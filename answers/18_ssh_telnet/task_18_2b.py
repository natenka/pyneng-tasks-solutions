# -*- coding: utf-8 -*-
"""
Задание 18.2b

Скопировать функцию send_config_commands из задания 18.2a и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка, функция должна выводить
сообщение на стандартный поток вывода с информацией о том, какая ошибка возникла,
при выполнении какой команды и на каком устройстве, например:
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1

Ошибки должны выводиться всегда, независимо от значения параметра log.
При этом, параметр log по-прежнему должен контролировать будет ли выводиться сообщение:
Подключаюсь к 192.168.100.1...


Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате (примеры словарей ниже):
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.


Пример работы функции send_config_commands:

In [16]: commands
Out[16]:
['logging 0255.255.1',
 'logging',
 'a',
 'logging buffered 20010',
 'ip http server']

In [17]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Команда "a" выполнилась с ошибкой "Ambiguous command:  "a"" на устройстве 192.168.100.1

In [18]: pprint(result, width=120)
({'ip http server': 'config term
'
                    'Enter configuration commands, one per line.  End with CNTL/Z.
'
                    'R1(config)#ip http server
'
                    'R1(config)#',
  'logging buffered 20010': 'config term
'
                            'Enter configuration commands, one per line.  End with CNTL/Z.
'
                            'R1(config)#logging buffered 20010
'
                            'R1(config)#'},
 {'a': 'config term
'
       'Enter configuration commands, one per line.  End with CNTL/Z.
'
       'R1(config)#a
'
       '% Ambiguous command:  "a"
'
       'R1(config)#',
  'logging': 'config term
'
             'Enter configuration commands, one per line.  End with CNTL/Z.
'
             'R1(config)#logging
'
             '% Incomplete command.
'
             '
'
             'R1(config)#',
  'logging 0255.255.1': 'config term
'
                        'Enter configuration commands, one per line.  End with CNTL/Z.
'
                        'R1(config)#logging 0255.255.1
'
                        '                   ^
'
                        "% Invalid input detected at '^' marker.
"
                        '
'
                        'R1(config)#'})

In [19]: good, bad = result

In [20]: good.keys()
Out[20]: dict_keys(['logging buffered 20010', 'ip http server'])

In [21]: bad.keys()
Out[21]: dict_keys(['logging 0255.255.1', 'logging', 'a'])


Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"
"""
import re
from netmiko import ConnectHandler
import yaml

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "i"]
correct_commands = ["logging buffered 20010", "ip http server"]
commands = commands_with_errors + correct_commands


def send_config_commands(device, config_commands, log=True):
    good_commands = {}
    bad_commands = {}
    error_message = 'Команда "{}" выполнилась с ошибкой "{}" на устройстве {}'
    regex = "% (?P<errmsg>.+)"

    if log:
        print("Подключаюсь к {}...".format(device["host"]))
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        for command in config_commands:
            result = ssh.send_config_set(command, exit_config_mode=False)
            error_in_result = re.search(regex, result)
            if error_in_result:
                print(
                    error_message.format(
                        command, error_in_result.group("errmsg"), ssh.host
                    )
                )
                bad_commands[command] = result
            else:
                good_commands[command] = result
        ssh.exit_config_mode()
    return good_commands, bad_commands


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_config_commands(dev, commands))
