# -*- coding: utf-8 -*-


from task_11_1 import convert_mac


def convert_mac_list(mac_list, strict=False):
    converted_mac_list = []
    for mac in mac_list:
        try:
            new_mac = convert_mac(mac)
        except ValueError:
            if strict:
                raise
        else:
            converted_mac_list.append(new_mac)
    return converted_mac_list

