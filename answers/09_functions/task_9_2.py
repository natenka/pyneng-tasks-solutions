# -*- coding: utf-8 -*-
"""
Задание 9.2

Создать функцию check_ip, которая проверяет, что строка, которая была передана функции,
содержит правильный IP-адрес.

Адрес считается правильным, если он:
- состоит из 4 чисел (а не букв или других символов)
- числа разделены точкой
- каждое число в диапазоне от 0 до 255

У функции должен быть один параметр ip_addr, который ожидает строку с IP-адресом.
Функция должна возвращать True если адрес правильный, False иначе.

Проверить работу функции на строках в списке ip_list.
Пример работы функции:
In [3]: check_ip("10.1.1.1")
Out[3]: True

In [4]: check_ip("10.500.1.1")
Out[4]: False

In [5]: check_ip("10.a.b.1")
Out[5]: False

In [6]: check_ip("10.1.1.1.")
Out[6]: False

In [7]: check_ip("10.1.1.1.1")
Out[7]: False

In [8]: check_ip("10.1.1.")
Out[8]: False

In [9]: check_ip("10.1.1")
Out[9]: False

In [10]: for ip in ip_list:
    ...:     print(check_ip(ip))
    ...:
True
False
False
True
False

"""

ip_list = ["10.1.1.1", "10.3.a.a", "500.1.1.1", "150.168.100.1", "62.150.240.300"]

def check_ip(ip_addr):
    octets = ip_addr.split(".")

    if len(octets) != 4:
        return False
    else:
        for octet in octets:
            if not (octet.isdigit() and int(octet) in range(256)):
                return False
    return True


