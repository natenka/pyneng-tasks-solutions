# -*- coding: utf-8 -*-
"""
Задание 6.7

В скрипте сделан генератор конфигурации для access-портов.
Сделать аналогичный генератор конфигурации для портов trunk.

В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать,
что с ними делать (добавлять, удалять, перезаписывать).

Поэтому в соответствии каждому порту стоит список и первый (нулевой) элемент списка
указывает как воспринимать номера VLAN, которые идут дальше.

Пример значения и соответствующей команды:
* ['add', '10', '20'] - команда switchport trunk allowed vlan add 10,20
* ['del', '17'] - команда switchport trunk allowed vlan remove 17
* ['only', '11', '30'] - команда switchport trunk allowed vlan 11,30

Задача для портов 0/1, 0/2, 0/4, 0/5, 0/7:
- сгенерировать конфигурацию на основе шаблона trunk_template
- с учетом ключевых слов add, del, only

Код не должен привязываться к конкретным номерам портов. То есть,
если в словаре trunk будут другие номера интерфейсов, код должен работать.

Для данных в словаре trunk_template вывод на
стандартный поток вывода должен быть таким:
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,20
interface FastEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 11,30
interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan remove 17
interface FastEthernet0/5
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,21
interface FastEthernet0/7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30


На стандартный поток вывода надо выводить только команды trunk настройки,
а access закомментировать.

"""

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {
    "0/1": ["add", "10", "20", "30", "40"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"],
    "0/5": ["add", "10", "21"],
    "0/7": ["only", "30"],
}

for intf, value in trunk.items():
    print(f"interface FastEthernet{intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            action = value[0]
            vlans = ",".join(value[1:])

            if action == "add":
                print(f" {command} add {vlans}")
            elif action == "only":
                print(f" {command} {vlans}")
            elif action == "del":
                print(f" {command} remove {vlans}")
        else:
            print(f" {command}")


# этот вариант использует словарь, вместо if/else
trunk_actions = {"add": " add", "del": " remove", "only": ""}

for intf, value in trunk.items():
    print(f"interface FastEthernet{intf}")

    for command in trunk_template:
        if command.endswith("allowed vlan"):
            action = value[0]
            vlans = ",".join(value[1:])
            print(f" {command}{trunk_actions[action]} {vlans}")
        else:
            print(f" {command}")

# вариант с заменой
for intf, allowed in trunk.items():
    action = (
        allowed[0].replace("only", "").replace("del", " remove").replace("add", " add")
    )
    vlans = ",".join(allowed[1:])

    print(f"interface FastEthernet{intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            print(f" {command}{action} {vlans}")
        else:
            print(f" {command}")
