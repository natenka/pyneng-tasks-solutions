# -*- coding: utf-8 -*-

def convert_mac(mac_address):
    msg = f"'{mac_address}' does not appear to be a MAC address"
    mac = mac_address.strip()
    sep = ":-."
    for s in sep:
        mac = mac.replace(s, " ")

    parts = mac.split(" ")
    if len(parts) not in (1, 3):
        raise ValueError(msg)
    elif len(parts) == 3:
        if not all([len(part) == 4 for part in parts]):
            raise ValueError(msg)

    mac = mac.replace(" ", "")
    if len(mac) != 12:
        raise ValueError(msg)
    for sym in mac:
        if sym.lower() not in "abcdef0123456789":
            raise ValueError(msg)

    new_mac = []
    for index in range(0, len(mac), 2):
        part = mac[index: index + 2]
        new_mac.append(part)
    return ":".join(new_mac)


def convert_mac(mac_address):
    formats = [
        "xxxxxxxxxxxx",
        "xxxx:xxxx:xxxx",
        "xxxx.xxxx.xxxx",
        "xxxx-xxxx-xxxx",
    ]
    separators = ":-."
    new_mac = ""
    for sym in mac_address:
        if sym in separators:
            new_mac += sym
        elif sym.lower() in "abcdef0123456789":
            new_mac += "x"
        else:
            raise ValueError(f"'{mac_address}' does not appear to be a MAC address")

    if new_mac not in formats:
        raise ValueError(f"'{mac_address}' does not appear to be a MAC address")

    for s in separators:
        mac_address = mac_address.replace(s, "")

    final_mac = []
    for index in range(0, len(mac_address), 2):
        part = mac_address[index: index + 2]
        final_mac.append(part)
    return ":".join(final_mac)

