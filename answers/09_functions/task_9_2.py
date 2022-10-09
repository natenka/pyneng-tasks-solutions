# -*- coding: utf-8 -*-


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


