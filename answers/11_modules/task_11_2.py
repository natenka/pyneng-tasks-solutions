"""
Задание 11.2

Создать функцию prompt_user_ip которая запрашивает пользователя ввод IP-адреса,
проверяет правильность введенного адреса и, если он неправильный, запрашивает
адрес снова. Если пользователь ввел правильный IP-адрес, функция возвращает его.

У функции prompt_user_ip должны быть такие параметры:
* max_retry - ожидает как аргумент список с MAC-адресами. Значение по умолчанию 5.
* ensure_unicast - параметр, который контролирует, что делать с неправильными
  Возможные значения True/False. Значение по умолчанию False.

IP-адрес считается правильным, если он:
- состоит из 4 чисел (а не букв или других символов)
- числа разделены точкой
- каждое число в диапазоне от 0 до 255


Пример работы функции:

In [7]: prompt_user_ip(max_retry=5, ensure_unicast=False)
Введите правильный IP-адрес: 10.1.1.1.1
Неправильный IP-адрес
Введите правильный IP-адрес: 10.1.1.1
Out[7]: '10.1.1.1'

In [8]: prompt_user_ip(max_retry=5, ensure_unicast=False)
Введите правильный IP-адрес: 110.1.500.1
Неправильный IP-адрес
Введите правильный IP-адрес: 4.4.4.4
Out[8]: '4.4.4.4'

In [9]: prompt_user_ip(max_retry=3, ensure_unicast=False)
Введите правильный IP-адрес: a
Неправильный IP-адрес
Введите правильный IP-адрес: a
Неправильный IP-адрес
Введите правильный IP-адрес: a
Неправильный IP-адрес
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: После 3 попыток не был введен правильный адрес

In [10]: prompt_user_ip(max_retry=5, ensure_unicast=True)
Введите правильный IP-адрес: 255.255.255.255
Введите IP-адрес в диапазоне unicast: 1-223
Введите правильный IP-адрес: 10.1.1.1
Out[10]: '10.1.1.1'

In [12]: prompt_user_ip(max_retry=3, ensure_unicast=True)
Введите правильный IP-адрес: 0.0.0.0
Введите IP-адрес в диапазоне unicast: 1-223
Введите правильный IP-адрес: 0.0.0.0
Введите IP-адрес в диапазоне unicast: 1-223
Введите правильный IP-адрес: 0.0.0.0
Введите IP-адрес в диапазоне unicast: 1-223
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: После 3 попыток не был введен правильный адрес

"""


def check_ip(ip_addr):
    octets = ip_addr.split(".")

    if len(octets) != 4:
        return False
    else:
        for octet in octets:
            if not (octet.isdigit() and int(octet) in range(256)):
                return False
    return True


def prompt_user_ip(max_retry=5, ensure_unicast=False):
    for _ in range(max_retry):
        ip = input("Введите правильный IP-адрес: ")
        if check_ip(ip):
            if ensure_unicast:
                octet1 = int(ip.split(".")[0])
                if 1 <= octet1 <= 223:
                    return ip
                else:
                    print("Введите IP-адрес в диапазоне unicast: 1-223")
            else:
                return ip
        else:
            print(f"Неправильный IP-адрес")
    raise ValueError(f"После {max_retry} попыток не был введен правильный адрес")

