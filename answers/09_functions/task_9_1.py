# -*- coding: utf-8 -*-
"""
Задание 9.1

Создать функцию convert_mac, которая конвертирует MAC-адрес из формата
1a1b.2c2d.3e3f в 1a:1b:2c:2d:3e:3f.

У функции должен быть один параметр: mac_address, который ожидает строку с
MAC-адресом в формате 1a1b.2c2d.3e3f.  Функция должна возвращать строку с
MAC-адресом в формате 1a:1b:2c:2d:3e:3f.

Проверить работу функции на разных MAC-адресах в списке mac_list.

В этом задании можно не проверять, что MAC-адрес, который передается функции
как аргумент записан в формате "aaaa.bbbb.cccc". Это будет сделано в задании 11го
раздела.

Пример работы функции:

In [4]: convert_mac("1a1b.2c2d.3e3f")
Out[4]: '1a:1b:2c:2d:3e:3f'

In [5]: convert_mac("1111.2222.3333")
Out[5]: '11:11:22:22:33:33'

In [6]: mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

In [7]: for m in mac_list:
   ...:     print(convert_mac(m))
   ...:
1a:1b:2c:2d:3e:3f
aa:aa:bb:bb:cc:cc
11:11:22:22:33:33

"""

mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

def convert_mac(mac_address):
    mac = mac_address.replace(".", "")
    new_mac = []
    for index in range(0, len(mac), 2):
        part = mac[index: index + 2]
        new_mac.append(part)
    return ":".join(new_mac)

