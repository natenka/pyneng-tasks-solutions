# -*- coding: utf-8 -*-
"""
Задание 11.1

Сделать функцию convert_mac которая конвертирует mac-адрес из разных форматов в
1a:1b:2c:2d:3e:3f.
У функции должен быть один параметр: mac_address, который ожидает строку с
MAC-адресом в одном из форматов ниже.  Функция должна возвращать строку с
MAC-адресом в формате 1a:1b:2c:2d:3e:3f.

Должна поддерживаться конвертация из таких форматов:
* 1a1b2c2d3e3f
* 1a1b:2c2d:3e3f
* 1a1b.2c2d.3e3f
* 1a-1b-2c-2d-3e-3f
* 1a.1b.2c.2d.3e.3f
* 1a1b-2c2d-3e3f
* 1a:1b:2c:2d:3e:3f (оставить без изменений)

Функция также должна проверять, что строка, которая была передана функции,
содержит правильный MAC-адрес. MAC-адрес считается правильным, если он:
- записан в одном из поддерживаемых форматов
- каждый символ, кроме разделителей ":,-.", это символ в диапазоне a-f или 0-9
- не считая разделители, в MAC-адресе должно быть 12 символов

Если как аргумент была передана строка, которая не содержит правильный
MAC-адрес, сгенерировать исключение ValueError (... должно быть заменено на
переданное значение, примеры ниже): ValueError: '...' does not appear to be a
MAC address

Проверить работу функции на разных MAC-адресах в списке mac_list.

Пример работы функции:

In [2]: convert_mac("1a1b.2c2d.3e3f")
Out[2]: '1a:1b:2c:2d:3e:3f'

In [3]: convert_mac("1111.2222.3333")
Out[3]: '11:11:22:22:33:33'

In [4]: convert_mac("111122223333")
Out[4]: '11:11:22:22:33:33'

In [5]: convert_mac("1111-2222-3333")
Out[5]: '11:11:22:22:33:33'

In [6]: convert_mac("1111-2222-33")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [6], in <cell line: 1>()
----> 1 convert_mac("1111-2222-33")
...
ValueError: '1111-2222-33' does not appear to be a MAC address


In [7]: convert_mac("1111-2222-33WW")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [7], in <cell line: 1>()
----> 1 convert_mac("1111-2222-33WW")
...
ValueError: '1111-2222-33WW' does not appear to be a MAC address

"""

def convert_mac(mac_address):
    mac = mac_address.strip()
    sep = ":,-."
    for s in sep:
        mac = mac.replace(s, "")
    if len(mac) != 12:
        raise ValueError(f"'{mac_address}' does not appear to be a MAC address")
    for sym in mac:
        if sym.lower() not in "abcdef0123456789":
            raise ValueError(f"'{mac_address}' does not appear to be a MAC address")

    new_mac = []
    for index in range(0, len(mac), 2):
        part = mac[index: index + 2]
        new_mac.append(part)
    return ":".join(new_mac)


