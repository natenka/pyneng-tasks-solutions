# -*- coding: utf-8 -*-
"""
Задание 9.6a

Сделать копию функции get_int_vlan_map из задания 9.6.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt
Пример работы функции
In [2]: get_int_vlan_map("config_sw2.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30,
  'FastEthernet1/3': 1,
  'FastEthernet2/0': 1,
  'FastEthernet2/1': 1},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [4]: access, trunk = get_int_vlan_map("config_sw2.txt")

In [5]: access
Out[5]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30,
 'FastEthernet1/3': 1,
 'FastEthernet2/0': 1,
 'FastEthernet2/1': 1}

In [6]: trunk
Out[6]:
{'FastEthernet0/1': [100, 200],
 'FastEthernet0/3': [100, 300, 400, 500, 600],
 'FastEthernet1/2': [400, 500, 600]}


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

def get_int_vlan_map(config_filename):
    access_port_dict = {}
    trunk_port_dict = {}
    with open(config_filename) as f:
        for line in f:
            if line.startswith("interface FastEthernet"):
                current_interface = line.split()[-1]
                # Сразу указываем, что интерфейсу
                # соответствует 1 влан в access_port_dict
                access_port_dict[current_interface] = 1
            elif "switchport access vlan" in line:
                # если нашлось другое значение VLAN,
                # оно перепишет предыдущее соответствие
                access_port_dict[current_interface] = int(line.split()[-1])
            elif "switchport trunk allowed vlan" in line:
                vlans = [int(i) for i in line.split()[-1].split(",")]
                trunk_port_dict[current_interface] = vlans
                # если встретилась команда trunk allowed vlan
                # надо удалить интерфейс из словаря access_port_dict
                del access_port_dict[current_interface]
    return access_port_dict, trunk_port_dict

