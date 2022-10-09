# -*- coding: utf-8 -*-
"""
Задание 4.2

Если запустить код задания, будет такой вывод:
$ python task_4_2.py
ip nat inside source list ACL interface FastEthernet0/1 overload

Надо преобразовать строку nat таким образом, чтобы на экран была выведена такая
строка (заменен тип интерфейса с FastEthernet на GigabitEthernet и строка
переведена в нижний регистр):

$ python task_4_2.py
ip nat inside source list acl interface gigabitethernet0/1 overload

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.

"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat_gig = nat.replace("Fast", "Gigabit")
print(nat_gig.lower())

# вариант
# nat_gig = nat.lower().replace("fast", "gigabit")
# print(nat_gig)
