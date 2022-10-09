# -*- coding: utf-8 -*-
"""
Задание 6.4

Список files содержит имена файлов:
["cfg_1.txt", "cfg_4.txt", "cfg_8.txt", "cfg_9.txt", "cfg_12.txt", "cfg_15.txt"]

Надо переименовать файлы таким образом:
["cfg_01.txt", "cfg_04.txt", "cfg_08.txt", "cfg_09.txt", "cfg_12.txt", "cfg_15.txt"]

То есть надо сделать так, чтобы после cfg_ всегда были две цифры. Если число
меньше 10, дополнить до 2 цифр нулями в начале.

Написать код, который преобразует имена файлов в нужный формат и добавляет их в
новый список result (тест будет проверять переменную result).
Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.

Исходный список files нельзя менять вручную, все изменения надо сделать с помощью Python.
"""

files = [
    "cfg_1.txt", "cfg_4.txt", "cfg_8.txt", "cfg_9.txt", "cfg_12.txt", "cfg_15.txt"
]

result = []
for file in files:
    name = file.split(".")[0]
    num = name.split("_")[-1]
    new_num = "{:02}".format(int(num))
    new_name = file.replace(num, new_num)
    result.append(new_name)
print(result)

result = []
for file in files:
    name, ext = file.split(".")
    name_part, num = name.split("_")
    new_num = f"{int(num):02}"
    new_name = f"{name_part}_{new_num}.{ext}"
    result.append(new_name)
print(result)
