# -*- coding: utf-8 -*-
"""
Задание 5.3b

Переделать скрипт из задания 5.3a таким образом, чтобы, при запросе параметра,
отображался список возможных параметров. Список параметров надо получить из словаря,
а не прописывать вручную.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_5_3b.py
Введите имя устройства: r1
Введите имя параметра (location, vendor, model, ios, ip): ip
10.255.0.1

$ python task_5_3b.py
Введите имя устройства: sw1
Введите имя параметра (location, vendor, model, ios, ip, vlans, routing): ip
10.255.0.101

Ограничение: нельзя изменять словарь london_co.

Эту задачу можно решить без использования условия if.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}
device = input("Введите имя устройства: ")
params = ", ".join(london_co[device].keys())
parameter = input(f"Введите имя параметра ({params}): ")

print(london_co[device][parameter])
