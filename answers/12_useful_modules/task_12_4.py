# -*- coding: utf-8 -*-



from ipaddress import ip_address


def find_n_ip(ip_from_range1, range1, range2):
    range_list = "-".join([range1, range2]).split("-")
    start1, end1, start2, end2 = [ip_address(i) for i in range_list]

    ip = ip_address(ip_from_range1)

    current_ip = start1
    index = 0
    while True:
        if current_ip == ip:
            break
        elif current_ip > end1:
            raise ValueError(f"IP {ip} не в диапазоне {range1}")
        index += 1
        current_ip += 1

    match_ip = start2
    for _ in range(index):
        match_ip += 1
    if match_ip > end2:
        raise ValueError(f"Найденный IP {match_ip} не в диапазоне {range2}")
    return str(match_ip)


def find_n_ip(ip_from_range1, range1, range2):
    range_list = "-".join([range1, range2]).split("-")
    start1, end1, start2, end2 = [int(ip_address(i)) for i in range_list]
    ip = int(ip_address(ip_from_range1))
    if ip > end1:
        raise ValueError(f"IP {ip} не в диапазоне {range1}")

    index = ip - start1
    match_ip = start2 + index
    if match_ip > end2:
        raise ValueError(f"Найденный IP {match_ip} не в диапазоне {range2}")
    return str(ip_address(match_ip))


if __name__ == "__main__":
    print(find_n_ip("10.1.1.127", "10.1.1.100-10.1.2.200", "50.1.1.110-50.1.2.210"))
