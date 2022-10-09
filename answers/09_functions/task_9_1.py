# -*- coding: utf-8 -*-


mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

def convert_mac(mac_address):
    mac = mac_address.replace(".", "")
    new_mac = []
    for index in range(0, len(mac), 2):
        part = mac[index: index + 2]
        new_mac.append(part)
    return ":".join(new_mac)

