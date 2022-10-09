# -*- coding: utf-8 -*-

ip = "192.168.3.1"

octets = ip.split(".")

output = """
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

print(output.format(int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3])))
