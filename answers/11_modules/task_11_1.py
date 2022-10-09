# -*- coding: utf-8 -*-


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


