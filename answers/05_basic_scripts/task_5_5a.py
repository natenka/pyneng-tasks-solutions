# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Плюсом будет решить задание без использования условия if и цикла for,
но первый вариант решения лучше сделать так, как будет получаться.
"""

access_template = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

trunk_template = """switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""

template = {"access": access_template, "trunk": trunk_template}
question = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы: "}

mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")
vlans = input(question[mode])

print("interface {}".format(interface))
print(template[mode].format(vlans))
