# -*- coding: utf-8 -*-
"""
Задание 7.4

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
получать из него информацию о портах в режиме trunk и вланах, которые настроены
на этих портах.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_4.py config_trunk_sw2.txt
$ python task_7_4.py config_trunk_sw3.txt

Передавать имя файла как аргумент скрипту. Указанный конфиг надо обработать и
получить словарь портов в режиме trunk, где ключи номера портов,
а значения список разрешенных VLAN (список строк).

Записать итоговый словарь в переменную trunk_dict (именно эта переменная будет
проверяться в тесте). По желанию можно выводить словарь на экран, тест
проверяет только содержимое переменной. Тут удобно выводить словарь с помощью pprint.

Например, для файла config_trunk_sw2.txt должен получиться такой словарь:

$ python task_7_4.py config_trunk_sw2.txt
{'FastEthernet0/1': ['100', '200'],
 'FastEthernet0/3': ['100', '300', '400', '500', '600'],
 'FastEthernet0/4': ['400', '500', '600']}

Для файла config_trunk_sw3.txt должен получиться такой словарь:
$ python task_7_4.py config_trunk_sw3.txt
{'FastEthernet0/1': ['10', '20', '21', '22'],
 'FastEthernet0/2': ['10', '13', '1450', '1451', '1452'],
 'FastEthernet0/6': ['40', '50', '60']}


Проверить работу функции на примере файлов config_trunk_sw2.txt и config_trunk_sw3.txt.
Убедиться, что для этих файлов получаются правильные словари.

Подсказка по синтаксису cisco: в этом задании считаем, что интерфейс находится
в режиме trunk, если у него настроена команда switchport trunk allowed vlans.
"""
from pprint import pprint
import sys

config = sys.argv[1]
trunk_dict = {}
with open(config) as cfg:
    for line in cfg:
        line = line.rstrip()
        if line.startswith("interface"):
            intf = line.split()[1]
        elif "trunk allowed" in line:
            trunk_dict[intf] = line.split()[-1].split(",")
pprint(trunk_dict)

