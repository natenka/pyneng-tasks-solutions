# -*- coding: utf-8 -*-

"""
Задание 24.2

Создать класс MyNetmiko, который наследует класс CiscoIosSSH из netmiko.

Переписать метод __init__ в классе MyNetmiko таким образом, чтобы после подключения
по SSH выполнялся переход в режим enable.

Для этого в методе __init__ должен сначала вызываться метод __init__ класса CiscoIosSSH,
а затем выполнятся переход в режим enable.

Проверить, что в классе MyNetmiko доступны методы send_command и send_config_set
(они наследуются автоматически, это только для проверки).

In [2]: from task_24_2 import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up      
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up      
Ethernet0/2                190.16.200.1    YES NVRAM  up                    up      
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up      
Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up      
Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up      
Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

"""
from netmiko.cisco.cisco_ios import CiscoIosSSH


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()
